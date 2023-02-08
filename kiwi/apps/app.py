from kiwi.core import SysLoader, Environment


class KiwiCoder:
    def __init__(self):
        self.environment = Environment()
        self.sys_loader = SysLoader()

    def run(self) -> None:
        """
        init watcher and connectors
        """
        self.sys_loader.build_sys()
