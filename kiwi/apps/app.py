from kiwi.cli import Cmd
from threading import Thread
from kiwi.core.kiwi_sys import GenericEnv, KiwiSys


class KiwiCoder:
    def __init__(self):
        self.environment = GenericEnv()
        self.kiwi_sys = KiwiSys()
        self.cmd = Cmd(self.kiwi_sys)

    def __del__(self):
        self.cmd_thread.join()

    def run(self) -> None:
        self.kiwi_sys.build_sys()
        self._run_cmd()

    def run_all(self) -> None:
        self.kiwi_sys.build_sys()
        self.kiwi_sys.task_scanner_callback()
        self.kiwi_sys.run_task_callback()

    def _run_cmd(self) -> None:
        self.cmd_thread = Thread(target=self.cmd.run)
        self.cmd_thread.start()
