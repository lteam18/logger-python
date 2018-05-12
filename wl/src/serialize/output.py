def logFile(filePath):
    def log(msg):
        fo = open(filePath, "a+")
        fo.write(msg)
        fo.write('\n')
        fo.close()

    return log


def logConsole():
    def log(msg):
        print(msg)
        
    return log

def combine(funcList):
    def log(msg):
        for func in funcList:
            func(msg)

    return log

CONSOLE = logConsole()
    
    
        
    
    
