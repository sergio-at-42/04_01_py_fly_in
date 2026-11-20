__version__ = "1.0.0"
__author__ = "Serge"

__all__ = ["Error",
           "DataTypeError",
           "DataKeyError",
           "DataValueError",
           "DataError",
           "Parser",
           "Zone",
           "Connection"]

from .error import Error, \
    DataTypeError, \
    DataKeyError, \
    DataValueError, \
    DataError

from .parser import Parser

from .zone import Zone

from .connection import Connection