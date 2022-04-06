import logging


def get_handler():
    handler: logging.Handler = logging.handlers.StreamHandler(address='/dev/log')
    handler.setLevel(logging.INFO)
    return handler
