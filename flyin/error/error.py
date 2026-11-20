#!/usr/bin/env python3

from __future__ import annotations
from datetime import datetime
from typing import Any


class Error(Exception):
    """Base class for related errors."""

    log_file_name: str = "error.log"
    new_log: bool = True

    def __init__(self, log_msg: str) -> None:
        super().__init__(log_msg)
        if self.new_log:
            self.log_application_started()
        self.write_log(log_msg)

    @classmethod
    def write_log(cls, log_msg: str) -> bool:
        write_ok: bool = False
        try:
            with open(cls.log_file_name, "a") as log_file:
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
        msg: str = ("[info]"
                    f"\t{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
                    "\tApplication started 🤖\n")
        write_ok: bool = False
        try:
            with open(cls.log_file_name, "a") as log_file:
                log_file.write(msg)
                cls.new_log = False
                write_ok = True
        except Exception:
            write_ok = False
        return (write_ok)

    @classmethod
    def log_game_over(cls) -> bool:
        msg: str = ("[info]"
                    f"\t{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
                    "\tGame Over 🎮👾\n\n")
        write_ok: bool = False
        try:
            with open(cls.log_file_name, "a") as log_file:
                log_file.write(msg)
                write_ok = True
        except Exception:
            write_ok = False
        return (write_ok)


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


class DataError(Error):
    """Base class for any related errors."""
    def __init__(self) -> None:
        super().__init__("[error]Class to create any errors.")
