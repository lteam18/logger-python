import sys
print(sys.path)
sys.path.append(".")
sys.path.append("./serialize")

from logger import Logger
import serialize.output as Output
import serialize.Serializer as Serializer

if __name__ == '__main__':
    root_logger = Logger.createRoot(
        'MainLogger-123',
        serializer = Serializer.combine([
            Serializer.Major(
                output = Output.combine(
                    [Output.CONSOLE, Output.logFile('a.log')]
                    )
            ),
            Serializer.Major(output = Output.logFile('b.log'))
        ])
    )
    logger = root_logger

    logger.debug(msg = "Program ready")

    logger.info(msg = "123", data = "a.1, b.2")
    
    sub_logger = root_logger.createSub('sublogger')

    logger.info(msg = "Hello", data = {
        "c": 1,
        "d": 2
    })


    

    

