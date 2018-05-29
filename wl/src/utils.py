import sys
import traceback


class ExceptionsLogger:
    def __init__(self, msg, name, stack):
        self.message = msg
        self.name = name
        self.stack = stack


def create_exception_info():
    info = sys.exc_info()
    stack = traceback.format_exc()
    return ExceptionsLogger(str(info[1]), str(info[0]), stack)


def convert_to_units(millis):
    units = []
    rest = (millis, 0)[millis < 0]

    ms = rest % 1000
    rest //= 1000
    if ms > 0:
        units.append(str(ms) + 'ms')

    s = rest % 60
    rest //= 60
    if s > 0:
        units.append(str(s) + 's')

    m = rest % 60
    rest //= 60
    if m > 0:
        units.append(str(m) + 'm')

    h = rest % 24
    rest //= 24
    if h > 0:
        units.append(str(h) + 'h')

    if rest > 0:
        units.append(str(rest) + 'd')

    if len(units) == 0:
        units.append('0ms')

    return reversed(units)


def format_diff_string(millis, max_string=9):
    arr = list(convert_to_units(millis))
    output = ''
    for s in arr:
        curr_len = len(output)
        if curr_len == 0 or curr_len + len(s) <= max_string:
            output += s
        else:
            return output
    return output


def convert(data, ret, prefix=""):
    if isinstance(data, list):
        print('is list')
        for i in range(0, len(data)):
            convert(data[i], ret, prefix + str(i) + '.')
    elif isinstance(data, dict):
        for key in data:
            convert(data[key], ret, prefix + str(key) + '.')
    else:
        s = '[%s]=%s' % (prefix[:-1], str(data))
        ret.append(s)

