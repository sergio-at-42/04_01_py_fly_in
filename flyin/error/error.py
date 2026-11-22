#!/usr/bin/env python3

from __future__ import annotations
from datetime import datetime
from typing import Any
from flyin.zone import Color


class Error(Exception):
    """Base class for related errors."""

    log_file_name: str = "error.log"
    new_log: bool = True
    log_msg: str = ""

    def __init__(self, log_msg: str) -> None:
        super().__init__(log_msg)
        Error.log_msg = log_msg
        if self.new_log:
            self.log_application_started()
        self.write_log(log_msg)

    @classmethod
    def write_log(cls, log_msg: str, write_type: str = "a") -> bool:
        write_ok: bool = False
        if write_type not in ["w", "a"]:
            write_type = "a"
        try:
            with open(cls.log_file_name, write_type) as log_file:
                msg_type, bracket, msg_text = log_msg.partition("]")
                if bracket == "":
                    msg_text = msg_type
                    msg_type = "[info]"
                else:
                    msg_type += bracket
                log_file.write(f"{msg_type}"
                               f"\t{datetime.now().strftime(
                                   "%Y-%m-%d %H:%M:%S")}"
                               f"\t{msg_text}\n")
                write_ok = True
        except Exception:
            write_ok = False
        return (write_ok)

    @classmethod
    def read_log(cls) -> str:
        log: str = ""
        try:
            with open(cls.log_file_name, "r") as log_file:
                log = log_file.read()
        except Exception:
            log = ""
        return (log)

    @classmethod
    def log_application_started(cls) -> bool:
        msg: str = ("[info]Application started 🤖")
        return (cls.write_log(msg, "w"))

    @classmethod
    def log_game_over(cls) -> bool:
        msg: str = ("[info]Game Over 🎮👾\n")
        return (cls.write_log(msg))

    @classmethod
    def print_and_exit(cls) -> None:
        msg: str = cls.log_msg
        spc: str = " " * ((80 - len(msg)) // 2)
        msg: str = spc + msg + spc
        danger: str = "   DANGER   DANGER   DANGER   DANGER   DANGER   DANGER   "
        panic: str = "              DON'T PANIC, IT'S JUST A BUG               "
        print(Color.NONE.ascii(), Color.BGRED.ascii(), Color.BLACK.ascii(), Color.DIMMED.ascii(), Color.BLINKING.ascii(), sep="", end="")
        print(danger.rjust((len(msg) + len(danger)) // 2).ljust(len(msg)))
        print(Color.NONE.ascii(), Color.BGBLACK.ascii(), Color.RED.ascii(), sep="", end="")
        print(msg)
        print(Color.NONE.ascii(), Color.BGRED.ascii(), Color.BLACK.ascii(), Color.DIMMED.ascii(), Color.BLINKING.ascii(), sep="", end="")
        print(panic.rjust((len(msg) + len(panic)) // 2).ljust(len(msg)))
        print(Color.NONE.ascii(), sep="", end="")
        exit(42)


class NoMapFileProvideError(Error):
    """Base class for map file related errors."""
    def __init__(self) -> None:
        super().__init__("[error]No map file provide.")


class MapFileNotFoundError(Error):
    """Base class for map file related errors."""
    def __init__(self, map_file: str = "") -> None:
        super().__init__(f"[error]Map file <{map_file}> not found.")


class ParserError(Error):
    """Base class for parser related errors."""
    def __init__(self, num_line: int, e: Error) -> None:
        super().__init__(f"Parser Error line {num_line} : {e}")


class DataTypeError(Error):
    """Base class for type related errors."""
    def __init__(self, key: str, value: Any, attended_key_type: type) -> None:
        super().__init__(f"[error]Submit key <{key}> with value <{value}> "
                         f"is type of <{type(key).__name__}>. "
                         f"<{attended_key_type.__name__}> attended.")


class DataKeyError(Error):
    """Base class for key related errors."""
    def __init__(self, key: str) -> None:
        super().__init__(f"[error]Submit key <{key}> not exist.")


class DataValueError(Error):
    """Base class for key related errors."""
    def __init__(self, key: str, value: Any) -> None:
        super().__init__(f"[error]<{value}> not a valid value "
                         f"for key <{key}>.")


class ParametersValueError(Error):
    """Base class for hub type related errors."""
    def __init__(self, value: str) -> None:
        super().__init__(f"[error]<{value}> not a valid value "
                         f"for parameters.")


class NbDroneError(Error):
    """Base class for nb drone less then 0  related errors."""
    def __init__(self) -> None:
        super().__init__("[error]Number of drone must be "
                         "a positive integer, greater than 1.")


class HubTypeError(Error):
    """Base class for hub type related errors."""
    def __init__(self, hub_type: str) -> None:
        super().__init__(f"[error]<{hub_type}> not a valid value "
                         f"for hub type.")


class StartHubExistError(Error):
    """Base class for start hub related errors."""
    def __init__(self) -> None:
        super().__init__("[error]Start Hub already exist "
                         "and must be unique.")


class EndHubExistError(Error):
    """Base class for end hub related errors."""
    def __init__(self) -> None:
        super().__init__("[error]End Hub already exist "
                         "and must be unique.")


class DashOrSpaceInZoneNameError(Error):
    """Base class for dashes or spaces in zone name related errors."""
    def __init__(self, zone_name: str) -> None:
        super().__init__("[error]invalid dashes or spaces"
                         f" in zone name <{zone_name}>.")


class CoordMustBeIntegerError(Error):
    """Base class for coord related errors."""
    def __init__(self) -> None:
        super().__init__("[error]X and Y coordinates must be integers.")


class ZoneExistError(Error):
    """Base class for zone exist related errors."""
    def __init__(self, zone_name: str) -> None:
        super().__init__(f"[error]zone <{zone_name}> already exist "
                         "and must be unique.")


class ZoneTypeError(Error):
    """Base class for zone type related errors."""
    def __init__(self, zone_type: str) -> None:
        super().__init__(f"[error]<{zone_type}> not a valid value "
                         f"for zone type.")


class NotValidColorError(Error):
    """Base class for hub type related errors."""
    def __init__(self, color: str) -> None:
        super().__init__(f"[error]<{color}> not a valid value "
                         f"for color.")


class ZoneNotExistError(Error):
    """Base class for zone in connection related errors."""
    def __init__(self, zone_name: str) -> None:
        super().__init__(f"[error]<{zone_name}> zone not exist "
                         "for connection.")


class SameZoneError(Error):
    """Base class for zone in connection related errors."""
    def __init__(self) -> None:
        super().__init__("[error]The 2 zones can not be the same "
                         "for a connection.")


class ConnectionExistError(Error):
    """Base class for start hub related errors."""
    def __init__(self) -> None:
        super().__init__("[error]Connection already exist "
                         "and must be unique.")
