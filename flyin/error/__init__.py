__version__ = "1.0.0"
__author__ = "Serge"

__all__ = ["Error",
           "DataTypeError",
           "DataKeyError",
           "DataValueError",
           "DataError"]

from .error import Error, \
    DataTypeError, \
    DataKeyError, \
    DataValueError, \
    DataError
