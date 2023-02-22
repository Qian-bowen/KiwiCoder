import asyncio
import inspect
import sys

from kiwi.core.bio_obj import BioObject
from typing import Dict, Callable
from kiwi.core.sched import StepController
from kiwi.common import singleton, ConstWrapper, ScheduleMode, ModuleNotFoundException, ClassNotFoundException, Config, \
    SysStatus, MsgLevel, MsgEndpoint, EventName, Msg, UserMsg
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

from kiwi.util import EventBus

bus = EventBus()


@singleton
class GenericEnv:
    """GenericEnv class handles user defined wrapper, and makes a basic environment"""

    def __init__(self):
        self.wrappers = []
        self.steps_generic = []
        self.periphery_generic = []
        self.overload_core_obj = set()

    def reset(self):
        self.__init__()

    def add_overload_obj(self, overload_name: str) -> None:
        self.overload_core_obj.add(overload_name)

    def append_wrapper(self, wrapper, *args, **kwargs):
        self.wrappers.append(wrapper)

    def build_wrapper(self):
        for wrapper in self.wrappers:
            self._wrapper2core(*wrapper.args, **wrapper.kwargs, wrapper=wrapper)

    def _wrapper2core(self, wrapper, *args, **kwargs):
        """ try to find user defined op class dynamically, or use the default one """
        if wrapper.class_name() in self.overload_core_obj:
            target_class_template = import_plugin_class(Config.USER_DEFINED_PACKAGE, wrapper.class_name())
        else:
            target_class_template = import_plugin_class(wrapper.package_name(), wrapper.class_name())
        ''' convert wrapper to core object '''
        if wrapper.get_wrapper_type() == ConstWrapper.STEP_WRAPPER:
            step = target_class_template(*args, **kwargs)
            self.steps_generic.append(step)
        elif ConstWrapper.is_op_wrapper(wrapper.get_wrapper_type()):
            op = None
            current_step = self.steps_generic[len(self.steps_generic) - 1]
            if wrapper.get_wrapper_type() == ConstWrapper.OP_MEASURE_FLUID_WRAPPER:
                op = target_class_template(step_name=current_step.step_num, op_index=len(current_step.operations),
                                           *args, **kwargs)
            current_step.append_operation(op)
        elif ConstWrapper.is_periphery_wrapper(wrapper.get_wrapper_type()):
            target_class = target_class_template(*args, **kwargs)
            self.periphery_generic.append(target_class)


@singleton
class KiwiSys:
    def __init__(self, thread_pool_size: int, schedule_mode=ScheduleMode.SEQ):
        self.obj_map = Dict[int, BioObject]
        self.obj_relation = Dict[BioObject, BioObject]
        self.step_controller = StepController(schedule_mode)
        self.thread_pool = ThreadPoolExecutor(max_workers=thread_pool_size)
        self.sys_var_map = Dict[str, Callable]

    def build_sys(self):
        """ prepare the system """
        self._init_sys_var_map()

    def shutdown_sys(self):
        pass

    def task_scanner(self):
        self._load_module()
        self._scan_user_defined_package()
        GenericEnv().build_wrapper()
        self._scan_env()

    def run_task(self):
        task_thread = Thread(target=self._thread_run_task)
        task_thread.start()

    def set_sys_variable(self, var_name: str, var_value) -> str:
        self.sys_var_map[var_name + "_setter"](var_value)
        val = self.sys_var_map[var_name + "_getter"]()
        if hasattr(val, 'name'):
            val = val.name
        return str(val)

    def get_sys_variable(self, var_name: str) -> str:
        val = self.sys_var_map[var_name + "_getter"]()
        if hasattr(val, 'name'):
            val = val.name
        return str(val)

    def _thread_run_task(self):
        while True:
            next_steps = self.step_controller.next_steps()
            if next_steps is None or len(next_steps) == 0:
                break
            all_step_task = [self.thread_pool.submit(next_step.execute) for next_step in next_steps]
            wait(all_step_task, return_when=ALL_COMPLETED)
            for step_task in all_step_task:
                status = step_task.result()
                # print("status:{}".format(status))

    def _init_endpoint(self):
        asyncio.get_event_loop().run_until_complete(self.serve())

    def _init_sys_var_map(self):
        def schedule_mode_getter(): return self.step_controller.schedule_mode

        def schedule_mode_setter(val): self.step_controller.schedule_mode = val

        self.sys_var_map = {
            "schedule_mode_getter": schedule_mode_getter,
            "schedule_mode_setter": schedule_mode_setter
        }

    def _scan_process(self):
        """scan steps and build process graph"""
        pass

    def _load_module(self):
        """ load basic modules """
        try:
            __import__(Config.USER_DEFINED_PACKAGE)
        except ImportError:
            raise ModuleNotFoundException(Config.USER_DEFINED_PACKAGE)

    def _scan_user_defined_package(self):
        """ all user defined function or class name into system """
        overload_msg = ""
        for name, obj in inspect.getmembers(sys.modules[Config.USER_DEFINED_PACKAGE]):
            if inspect.isclass(obj) or inspect.isfunction(obj):
                GenericEnv().add_overload_obj(name)
                overload_msg += name
        self._print_to_screen(UserMsg.SYS_SCAN_USER_DEFINED_OVERLOAD_TEMPLATE.format(overload_msg))

    def _scan_entity(self):
        """check reagents"""
        pass

    def _scan_env(self):
        for wrapper in GenericEnv().wrappers:
            if wrapper.get_wrapper_type() == ConstWrapper.STEP_WRAPPER:
                pass
        self.step_controller = StepController(schedule_mode=ScheduleMode.GRAPH)
        self.step_controller.add_step_list(GenericEnv().steps_generic)
        self.step_controller.print_step_tree()
        self.step_controller.add_step_list_to_graph(GenericEnv().steps_generic)

    def topology_view(self):
        pass

    def print_sys_init_log(self):
        self.step_controller.print_step_tree()

    def _print_to_screen(self, msg: str, code=SysStatus.SUCCESS, level=MsgLevel.INFO):
        bus.emit(event=EventName.SCREEN_PRINT_EVENT,
                 msg=Msg(msg=msg, source=MsgEndpoint.SYS, destinations=[MsgEndpoint.USER_TERMINAL],
                         code=code, level=level))


def import_plugin_class(module_name, class_name):
    """ dynamic load class from module """
    try:
        module = __import__(module_name, fromlist=[class_name])
    except ImportError:
        raise ModuleNotFoundException(module_name)
    try:
        target_class = getattr(module, class_name)
    except AttributeError:
        raise ClassNotFoundException(class_name)
    return target_class
