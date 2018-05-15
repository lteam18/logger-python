from logger import Logger
from serialize import Serializer, Output
from serialize import Stringify

import time
import utils

if __name__ == '__main__':
    root_logger = Logger.create_root('MainLogger-123',
                                     serializer=[
                                        Serializer.Major(level_log_stringify=Stringify.create_chalk(), output=
                                            [Output.CONSOLE, Output.log_file('a.log')]
                                            ),
                                        Serializer.Major(output=Output.log_file('b.log'))]
                                     )
    logger = root_logger

    logger.debug(msg="Program ready")

    logger.info(msg="123", data="a.1, b.2")

    sub_logger = root_logger.create_sub('sublogger')

    time.sleep(2)

    try:
        f = 1/0
    except Exception:
        e = utils.create_exception_info()
        sub_logger.error(msg = "Error1", trace = e)

    x = 0
    e = utils.create_exception_info()
    sub_logger.error(msg="Error2", trace=e)
