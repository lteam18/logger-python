import serialize.Serializer as Serializer
import time
import collections

class Logger(object):
    
    def __init__(self, nameList, serializer = Serializer.Major()):
            if (serializer == None):
                serializer = Serializer.Major()
            self.nameList = nameList
            self.serializer = serializer

    @classmethod  
    def createRoot(cls, name, serializer = Serializer.Major()):
        return Logger([name], serializer)

    def createSub(self, name):
        return Logger(self.nameList + [name], self.serializer)

    def _outputDict(self, level, msg, data, trace):
        dic = collections.OrderedDict()
        dic['N'] = self.nameList
        dic['T'] = int(time.time())
        dic['L'] = level
        if (msg != None):
            dic['M'] = msg
        if (data != None):
            dic['D'] = data
        if (trace != None):
            traceDic = collections.OrderedDict()
            if (trace.message != None):
                traceDic['msg'] = trace.message
            if (trace.name != None):
                traceDic['name'] = trace.name
            if (trace.stack != None):
                traceDic['stack'] = trace.stack
            dic['E'] = traceDic
        return dic
    

    def _writeLog(self, level, msg = None, data = None, trace = None):
        self.serializer.log(self._outputDict(level, msg, data, trace))
        

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
        

