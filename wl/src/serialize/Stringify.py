import time

history = time.time()
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
FUCHSIA = 35
CYAN = 36
WHITE = 37


def chalk_function(opt=0, front=30):
    def chalk_string(data):
        s = '\033[%d;%dm%s\033[0m' % (opt, front, data)
        return s

    return chalk_string


DEFAULT_CHALK_LEVEL_MAP = {
    0: chalk_function(front=GREEN),
    1: chalk_function(front=CYAN),
    2: chalk_function(front=YELLOW),
    3: chalk_function(opt=1, front=FUCHSIA),
    4: chalk_function(opt=1, front=RED),
}


def create_chalk(fmap=DEFAULT_CHALK_LEVEL_MAP, SEP=9,
                 LEADING_SPACE=" ", LEADING_CHARS="_"):
    global history
    history = time.time()

    def chalk(data):
        global history
        diff = int(data['T'] - history)
        history = data['T']
        general_text_fun = fmap[data['L']]
        # TODO format it
        diff_time_fun = chalk_function(front=BLUE)
        l_diff_time = diff_time_fun(diff)
        time_fun = chalk_function(front=WHITE)
        l_time = time_fun(data['T'])
        l_namelist = str(data['N'])
        if 'M' in data:
            l_msg = general_text_fun(data['M'])
            msg = l_diff_time + " " + l_time + " [" + l_namelist + "] " + l_msg
        if 'D' in data:
            l_data = general_text_fun(data['D'])
            msg += "\n" + l_data
        return msg.replace("\n", "\n" + LEADING_SPACE)

    return chalk
