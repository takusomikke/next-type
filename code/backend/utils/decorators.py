import logging
import contextlib
logger = logging.getLogger("deco")
from utils.logger import BulkLogger

def log_decorator():
    def _log_decorator(func):
        def wrapper(*args, **kwargs):
            with BulkLogger(logger.info) as w:
                with contextlib.redirect_stderr(w), contextlib.redirect_stdout(w):
                    return func(*args, **kwargs)
        return wrapper
    return _log_decorator
