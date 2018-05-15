def log_file(file_path):
    def log(msg):
        fo = open(file_path, "a+")
        fo.write(msg)
        fo.write('\n')
        fo.close()

    return log


def log_console():
    def log(msg):
        print(msg)

    return log


def combine(func_list):
    def log(msg):
        for func in func_list:
            func(msg)

    return log


CONSOLE = log_console()
