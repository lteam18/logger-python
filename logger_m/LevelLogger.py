import a

class LevelLogger(object):
    def __init__(self, level):
        self.level = level
    
    def o(msg, data, trace):
        print(msg)

