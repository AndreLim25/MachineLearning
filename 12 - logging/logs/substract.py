from logger import logging

def substract(a, b):
    logging.debug("The substraction operation is taking place.")
    return a - b

logging.debug("The substraction function is called.")
substract(10, 5)