from abc import abstractmethod

from kiwi.common import ConstWrapper, ParseParamException
from kiwi.core import GenericEnv


class Wrapper:
    def __init__(self, wrapper_type, *args, **kwargs):
        """attach the wrapper to environment"""
        self.wrapper_type = wrapper_type
        GenericEnv().append_wrapper(*args, **kwargs, wrapper=self)

    def get_wrapper_type(self):
        return self.wrapper_type


class Step(Wrapper):
    def __init__(self, comment: str, step_spec=""):
        step_num, wait_list, parallel_list = Step._parse_step_spec(step_spec)
        super().__init__(step_num=step_num, wait_list=wait_list, children_parallel_list=parallel_list,
                         wrapper_type=ConstWrapper.STEP_WRAPPER)
        self.comment = comment
        self.step_spec = step_spec

    @staticmethod
    def _parse_step_spec(step_spec: str) -> (str, [str], [str]):
        """
            step_spec: a string which denotes step num, wait list, and parallel list.
            step number: step hierarchy, e.g. 1.2.1
            wait list: the step must run after all the steps and its previous step finish, e.g. [1.1,2.3]
            children parallel list: the child steps of it can run in parallel. e.g [1.1,1.2,1.3]
            a simple example: sn:2 wt:[1.1] cp[2.1,2.2,2.3]
            this step is 2rd step, it can run after 1.1 finish, and 2.1,2.2,2.3 steps can run in parallel
        """
        sn = None
        wt = []
        cp = []
        param_list = step_spec.split(' ', 3)
        if len(param_list) > 3 or len(param_list) == 0:
            raise ParseParamException('param numbers is wrong')

        for i in range(0, len(param_list)):
            if param_list[i][0:3] == "sn:":
                sn = param_list[i][3:]
            elif param_list[i][0:3] == "wt:":
                wt_raw = param_list[i][4:-1]
                wt = wt_raw.split(',')
            elif param_list[i][0:3] == "cp:":
                cp_raw = param_list[i][4:-1]
                cp = cp_raw.split(',')
            else:
                raise ParseParamException('param is wrong')

        return sn, wt, cp


class Periphery(Wrapper):
    def __init__(self, wrapper_type, company=None, product_number=None, comment=None):
        """
        Periphery Wrapper can run only when company & pn are specified
        Args:
            comment: just notes
            company: which company produce the product
            product_number: the product number unique in a company
        """
        self.company = company
        self.pn = product_number
        self.comment = comment
        super().__init__(wrapper_type=wrapper_type)

    @abstractmethod
    def package_name(self) -> str:
        pass

    def class_name(self) -> str:
        comm_name = ConstWrapper.get_class_name(self.wrapper_type)
        return comm_name + self.company + self.pn


class ControlPeriphery(Periphery):
    def __init__(self, wrapper_type=ConstWrapper.PERIPHERY_CONTROL_WRAPPER, company="", product_number="",
                 comment=None):
        super().__init__(company=company, product_number=product_number, comment=comment, wrapper_type=wrapper_type)

    def package_name(self) -> str:
        return "kiwi.plugin.hardware.control"


class InstrumPeriphery(Periphery):
    def __init__(self, wrapper_type=ConstWrapper.PERIPHERY_INSTRUM_WRAPPER, company="", product_number="",
                 comment=None):
        super().__init__(company=company, product_number=product_number, comment=comment, wrapper_type=wrapper_type)

    def package_name(self) -> str:
        return "kiwi.plugin.hardware.instrum"


class SignalPeriphery(Periphery):
    def __init__(self, wrapper_type=ConstWrapper.PERIPHERY_SIGNAL_WRAPPER, company="", product_number="", comment=None):
        super().__init__(company=company, product_number=product_number, comment=comment, wrapper_type=wrapper_type)

    def package_name(self) -> str:
        return "kiwi.plugin.hardware.signal"


class FlowMeter(InstrumPeriphery):
    def __init__(self, company="", product_number="", comment=None):
        super().__init__(company=company, product_number=product_number,
                         comment=comment, wrapper_type=ConstWrapper.PERIPHERY_INSTRUM_FLOW_METER_WRAPPER)

    def package_name(self) -> str:
        return super().package_name()


class Container(Wrapper):
    def __init__(self):
        super().__init__(wrapper_type=ConstWrapper.ENTITY_CONTAINER_WRAPPER)


class Fluid(Wrapper):
    def __init__(self):
        super().__init__(wrapper_type=ConstWrapper.ENTITY_FLUID_WRAPPER)

# class Vol(Wrapper):
#     def __init__(self):
#         super().__init__(wrapper_type=ConstWrapper.QUANTITY_VOL_WRAPPER)
