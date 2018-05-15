import sys
import traceback


class ExceptionsLogger:
    def __init__(self, msg, name, stack):
        self.message = msg
        self.name = name
        self.stack = stack


def create_exception_info():
    info = sys.exc_info()
    stack = traceback.format_exc()
    return ExceptionsLogger(str(info[1]), str(info[0]), stack)
