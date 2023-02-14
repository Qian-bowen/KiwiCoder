from kiwi.cli import Cmd
from threading import Thread


class KiwiCoder:
    def __init__(self):
        # self.environment = GenericEnv()
        # self.sys_loader = SysLoader()
        self.cmd = Cmd()

    def run(self) -> None:
        cmd_thread = Thread(target=self.cmd.run)
        cmd_thread.setDaemon(True)
        cmd_thread.start()
        cmd_thread.join()

    # def _run(self) -> None:
        
