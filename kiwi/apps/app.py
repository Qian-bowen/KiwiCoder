from kiwi.core import SysLoader, GenericEnv


class KiwiCoder:
    def __init__(self):
        self.environment = GenericEnv()
        self.sys_loader = SysLoader()

    def run(self) -> None:
        """
        init watcher and connectors
        """
        self.sys_loader.build_sys()
        self.sys_loader.print_sys_init_log()

