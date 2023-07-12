import inspect
import logging


class BaseClass:


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)
        fileHander = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s : %(message)s")
        fileHander.setFormatter(formatter)
        logger.addHandler(fileHander)  # file handler object
        # to get text name in the errors

        logger.setLevel(logging.DEBUG)
        return logger
