import logging


try:
    int("aaa")
    print('0')
except:
    logging.exception("What is doing when exception happens.")
    print('ok')