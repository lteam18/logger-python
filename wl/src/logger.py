import serialize.Serializer as Serializer
import time
import collections


class Logger(object):

    def __init__(self, name_list, serializer=Serializer.Major()):
        self.nameList = name_list
        if isinstance(serializer, list):
            self.serializer = Serializer.combine(serializer)
        else:
            self.serializer = serializer

    @classmethod
    def create_root(cls, name, serializer=Serializer.Major()):
        return Logger([name], serializer)

    def create_sub(self, name):
        return Logger(self.nameList + [name], self.serializer)

    def _output_dict(self, level, msg, data, trace):
        dic = collections.OrderedDict()
        dic['N'] = self.nameList
        dic['T'] = int(time.time())
        dic['L'] = level
        if msg is not None:
            dic['M'] = msg
        if data is not None:
            dic['D'] = data
        if trace is not None:
            trace_dic = collections.OrderedDict()
            if trace.message is not None:
                trace_dic['msg'] = trace.message
            if trace.name is not None:
                trace_dic['name'] = trace.name
            if trace.stack is not None:
                trace_dic['stack'] = trace.stack
            dic['E'] = trace_dic
        return dic

    def _write_log(self, level, msg=None, data=None, trace=None):
        self.serializer.log(self._output_dict(level, msg, data, trace))

    def debug(self, msg=None, data=None, trace=None):
        self._write_log(0, msg, data, trace)

    def info(self, msg=None, data=None, trace=None):
        self._write_log(1, msg, data, trace)

    def warn(self, msg=None, data=None, trace=None):
        self._write_log(2, msg, data, trace)

    def error(self, msg=None, data=None, trace=None):
        self._write_log(3, msg, data, trace)

    def fatal(self, msg=None, data=None, trace=None):
        self._write_log(4, msg, data, trace)
