from logger import Logger
from serialize import Output
from serialize import Serializer

import utils

if __name__ == '__main__':
    root_logger = Logger.createRoot('MainLogger-123', \
                                    serializer=Serializer.combine([ \
                                        Serializer.Major(output=Output.combine( \
                                            [Output.CONSOLE, Output.logFile('a.log')] \
                                            )), \
                                        Serializer.Major(output=Output.logFile('b.log'))] \
                                        ) \
                                    )
    logger = root_logger

    logger.debug(msg="Program ready")

    logger.info(msg="123", data="a.1, b.2")

    sub_logger = root_logger.createSub('sublogger')

    try:
        f = 1/0
    except Exception:
        e = utils.createExceptionInfo()
        sub_logger.error(msg = "Error1", trace = e)

    x = 0
    e = utils.createExceptionInfo()
    sub_logger.error(msg="Error2", trace=e)
