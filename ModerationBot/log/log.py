import logging  


def get_logger(text, type_):
    logger = logging.getLogger(text)
    logger.setLevel(getattr(logging, type_))

    log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(log_format))

    logger.addHandler(handler)

    return logger