from kiwi.cli import Cmd
from threading import Thread
from kiwi.core.kiwi_sys import GenericEnv, KiwiSys


class KiwiCoder:
    def __init__(self):
        self.environment = GenericEnv()
        self.kiwi_sys = KiwiSys()
        self.cmd = Cmd(self.kiwi_sys)

    def run(self) -> None:
        self.kiwi_sys.build_sys()
        self._run_cmd()

    def _run_cmd(self) -> None:
        cmd_thread = Thread(target=self.cmd.run)
        cmd_thread.setDaemon(True)
        cmd_thread.start()
        cmd_thread.join()
