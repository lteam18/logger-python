import json
from serialize import Output

class Major(object):
    
    def __init__(self, levelLogStringify = json.dumps, \
                 output = Output.CONSOLE):
        self.levelLogStringify = levelLogStringify
        if isinstance(output, list):
            self.output = Output.combine(output)
        else:
            self.output = output

    def log(self, data):
        self.output(self.levelLogStringify(data))

def combine(serializers):
    return Combination(serializers)

class Combination(object):

    def __init__(self, serializers):
        self.serializers = serializers

    def log(self, data):
        for s in self.serializers:
            s.log(data)
