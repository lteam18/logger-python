import LevelLogger

class Logger(object):
    def __init__(self):
        self.debug = LevelLogger()
        self.info = LevelLogger()
        self.warn = LevelLogger()
        self.error = LevelLogger()
        self.fatal = LevelLogger()

