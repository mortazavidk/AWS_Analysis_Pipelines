import logging

logging.basicConfig(filename="logfile.log", level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


""" 
add_logger is a closure. The add_logger is a function object that is binded
to log_func() and has access to the encolsing variable (func). 
The add_logger will be alive even the logger function has been destroyed.  
"""
add_logger = logger(add)
sub_logger = logger(sub)

add_logger(2, 3)
sub_logger(3, 2)
