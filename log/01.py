import logging


LOG_FORMAT = "%(asctime)s======%(levelname)s+++++++++%(message)s"

logging.basicConfig(level=logging.DEBUG,filename='test.log',format=LOG_FORMAT)

logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")


logging.log(logging.DEBUG,"this is debug log")
logging.log(logging.INFO,"this is info log")
logging.log(logging.WARNING,"this is warning log")
logging.log(logging.ERROR,"this is error log")
logging.log(logging.CRITICAL,"this is critical log")