import pkgutil

from . import utils

__path__ = pkgutil.extend_path(__path__, __name__)
print(__path__, __name__)
