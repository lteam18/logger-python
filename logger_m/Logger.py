
class Logger(object):
    def __init__(self):
        pass

    def _writeLog(self, level, msg = None, data = None, trace = None):
        pass

    def debug(self, msg = None, data = None, trace = None):
        self._writeLog(0, msg, data, trace)

    def info(self, msg = None, data = None, trace = None):
        self._writeLog(1, msg, data, trace)

    def warn(self, msg = None, data = None, trace = None):
        self._writeLog(2, msg, data, trace)

    def error(self, msg = None, data = None, trace = None):
        self._writeLog(3, msg, data, trace)

    def fatal(self, msg = None, data = None, trace = None):
        self._writeLog(4, msg, data, trace)

