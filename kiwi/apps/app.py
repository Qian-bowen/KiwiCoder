from threading import Thread

from kiwi.cli.command import Cmd
from kiwi.core.kiwi_sys import ProtocolGeneric, KiwiSys
from kiwi.common import ScheduleMode


class KiwiCoder:
    def __init__(self):
        self.environment = ProtocolGeneric()
        self.kiwi_sys = KiwiSys(thread_pool_size=10, schedule_mode=ScheduleMode.GRAPH)
        self.cmd = Cmd(self.kiwi_sys)

    def __del__(self):
        if self.cmd_thread is not None:
            self.cmd_thread.join()
        if self.printer_thread is not None:
            self.printer_thread.join()
        if self.server_thread is not None:
            self.server_thread.join()

    def run(self) -> None:
        self._run_printer()
        self._run_cmd()
        self._run_server()
        self.kiwi_sys.build_sys()

    def run_all(self) -> None:
        self._run_printer()
        self.kiwi_sys.build_sys()
        self.kiwi_sys.task_scanner()
        self.kiwi_sys.run_task()

    def _run_cmd(self) -> None:
        self.cmd_thread = Thread(target=self.cmd.run)
        self.cmd_thread.start()

    def _run_printer(self) -> None:
        self.printer_thread = Thread(target=self.cmd.output.printer)
        self.printer_thread.start()

    def _run_server(self) -> None:
        self.server_thread = Thread(target=self.kiwi_sys.server.serve)
        self.server_thread.start()
