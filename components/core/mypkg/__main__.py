import logging

from . import plugin

def common_setup():
    logging.info("Common setup")
    ...

common_setup()
plugin.setup()
