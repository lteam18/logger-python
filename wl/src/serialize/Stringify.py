def chalkString(data, opt = 0, front = 30, back = 30):
    s = '\033[%d;%d;%dm%s\033[0m' %(opt, front, back, data)
    return s


def createChalk():
    #TODO implement it
    def chalk(data):
        pass
    return chalk


print (chalkString('hello world', opt = 1,front = 31, back = 42))



