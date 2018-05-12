import output
import json

class Major(object):
    
    def __init__(self, levelLogStringify = json.dumps, \
                 output = output.CONSOLE):
        self.levelLogStringify = levelLogStringify
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
