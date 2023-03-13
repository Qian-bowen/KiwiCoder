from pathlib import Path
import sys

init_file_content = \
    "# DO NOT MODIFY THIS FILE\n" \
    "from .protocol import *\n" \
    "from .override import *\n\n"

protocol_file_content = \
    "# define experiment protocol in this file\n" \
    "from kiwi.wrapper import Step, start_protocol, end_protocol\n\n" \
    "def kiwi_protocol():\n" \
    "\t\"\"\" Define experiment protocol. \"\"\"\n" \
    "\tstart_protocol(\"You should rename but do not remove it.\")\n" \
    "\tStep(\"example step 1\", \"sn:1\")\n" \
    "\tend_protocol()\n\n\n" \
    "def watch():\n" \
    "\twatch_list = []\n" \
    "\treturn watch_list\n\n\n" \
    "def alarm():\n" \
    "\talarm_list = []\n" \
    "\treturn alarm_list\n\n\n" \
    "def mock():\n" \
    "\tmock_bio_obj_list = {}\n" \
    "\tmock_op_list = {}\n" \
    "\treturn mock_bio_obj_list, mock_op_list\n\n\n"

override_file_content = \
    "# override core class in this file\n\n"

main_file_content = \
    "# DO NOT MODIFY THIS FILE\n" \
    "from kiwi import KiwiCoder as Coder\n\n\n" \
    "def run_kiwi():\n" \
    "\tkiwi_coder = Coder()\n" \
    "\tkiwi_coder.run()\n\n\n" \
    "def main():\n" \
    "\trun_kiwi()\n\n\n" \
    "if __name__ == \"__main__\":\n" \
    "\tmain()\n\n"


class Generator:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.folder_name = "keee-weee"

    def _generate_init_file(self, file):
        file.write(init_file_content)

    def _generate_protocol_file(self, file):
        file.write(protocol_file_content)

    def _generate_override_file(self, file):
        file.write(override_file_content)

    def _generate_main(self, file):
        file.write(main_file_content)

    def generate_project_folder(self):
        path = self.base_path + '/' + self.folder_name
        Path(path).mkdir()
        f = Path(path + "/__main__.py").open("w+")
        self._generate_main(f)
        f.close()
        Path(path + '/user').mkdir()
        f = Path(path + "/user/__init__.py").open("w+")
        self._generate_init_file(f)
        f.close()
        f = Path(path + "/user/protocol.py").open("w+")
        self._generate_protocol_file(f)
        f.close()
        f = Path(path + "/user/override.py").open("w+")
        self._generate_override_file(f)
        f.close()
        Path(path + '/report').mkdir()


def main():
    """ take folder path from commandline """
    generator = Generator(sys.argv[1])
    generator.generate_project_folder()


if __name__ == "__main__":
    main()
