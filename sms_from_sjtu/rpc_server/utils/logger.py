import logging
import sys


def logger_factory(name=None, level=logging.INFO):
    logger = logging.getLogger(name if name else __name__)
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        "[%(asctime)s][%(levelname)s]<%(name)s> | %(message)s",
        "%H:%M:%S"
    ))
    logger.addHandler(handler)
    return logger
