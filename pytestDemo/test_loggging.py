import logging

def test_loggingDemo():


    logger = logging.getLogger(__name__)



    fileHander = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s : %(message)s")
    fileHander.setFormatter(formatter)
    logger.addHandler(fileHander)         # file handler object
# to get text name in the errors
    logger.setLevel(logging.DEBUG)
    logger.debug("a debug statement is executed")
    logger.info("Information messages")
    logger.warning("something in the warning mode")
    logger.error("a major error has happened")
    logger.critical("critical issue")