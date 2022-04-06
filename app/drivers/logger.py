import logging
from logging import handlers


def get_handler():
    handler = handlers.SysLogHandler(address='/dev/log')
    handler.setLevel(logging.INFO)
    return handler
