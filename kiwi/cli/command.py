from queue import Queue
from kiwi.util import EventBus
from kiwi.common import EventName, Msg, Config
import msvcrt

bus = EventBus()


class Cmd:
    def __init__(self):
        self.output = Output(Config.OUTPUT_MSG_BUFFER_SIZE)

    def run(self):
        while True:
            try:
                raw_cmd = input("kiwi>")
                self._parse_cmd(raw_cmd)
            except (KeyboardInterrupt, EOFError):
                """ stop print to screen """
                self.output.set_can_print(False)

    def _parse_cmd(self, raw_cmd: str):
        cmd_segments = raw_cmd.split(' ')
        if cmd_segments[0] == "out":
            if cmd_segments[1] == "-o":
                self.output.set_can_print(True)
            elif cmd_segments[1] == "-c":
                self.output.set_can_print(False)

        print("command is: " + raw_cmd)


class Output:
    """ output is not thread-safe """

    def __init__(self, buffer_size: int):
        self.out_buffer = Queue(buffer_size)
        self.can_print = True

    @bus.on(event=EventName.SCREEN_PRINT_EVENT)
    def print_screen(self, msg: Msg):
            raw_str = str(msg)
            if self.can_print:
                print(raw_str)
            else:
                self.out_buffer.put(raw_str)


    def set_can_print(self, can_print: bool):
        """ output print buffered msg when open again """
        if not self.can_print:
            msg_num = self.out_buffer.qsize()
            for i in range(msg_num):
                if self.out_buffer.empty():
                    break
                msg = self.out_buffer.get()
                print(msg)
        self.can_print = can_print
