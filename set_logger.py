import logging

def set_logger(logger, error_logger):
    logger.setLevel(logging.INFO)
    error_logger.setLevel(logging.WARNING)
    
    formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')

    file_handler = logging.FileHandler('./logs/calculate.log')
    file_handler.setFormatter(formatter)

    error_file_handler = logging.FileHandler('./logs/error.log')
    error_file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    error_logger.addHandler(error_file_handler)