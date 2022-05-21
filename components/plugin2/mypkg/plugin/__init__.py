__all__ = ("setup",)

import logging

from mypkg import utils

def setup():
    utils.check_something()
    logging.info("plugin2 setup")
    ...
