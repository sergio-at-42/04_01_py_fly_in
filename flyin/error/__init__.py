__version__ = "1.0.0"
__author__ = "Serge"

__all__ = ["Error",
           "MapFileNotFoundError",
           "NoMapFileProvideError",
           "ParserError",
           "DataTypeError",
           "DataKeyError",
           "DataValueError",
           "DataError",
           "ParametersValueError",
           "NbDroneError",
           "HubTypeError",
           "StartHubExistError",
           "EndHubExistError",
           "DashOrSpaceInZoneNameError",
           "CoordMustBeIntegerError",
           "ZoneExistError",
           "ZoneTypeError",
           "NotValidColorError",
           "ZoneNotExistError",
           "SameZoneError"]

from .error import Error, \
    MapFileNotFoundError, \
    NoMapFileProvideError, \
    ParserError, \
    DataTypeError, \
    DataKeyError, \
    DataValueError, \
    DataError, \
    ParametersValueError, \
    NbDroneError, \
    HubTypeError, \
    StartHubExistError, \
    EndHubExistError, \
    DashOrSpaceInZoneNameError, \
    CoordMustBeIntegerError, \
    ZoneExistError, \
    ZoneTypeError, \
    NotValidColorError, \
    ZoneNotExistError, \
    SameZoneError
