import logging
import sys


def getLogger(name=None):
    logger = logging.getLogger(__name__ if not name else name)
    logger.setLevel(logging.INFO)
    hdlr = logging.StreamHandler(sys.stdout)
    hdlr.setFormatter(logging.Formatter(
        "[%(asctime)s][%(levelname)s]<%(name)s> | %(message)s",
        "%H:%M:%S"
    ))
    logger.addHandler(hdlr)
    return logger
