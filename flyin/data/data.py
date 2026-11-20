from __future__ import annotations
from typing import Any
import sys
from pathlib import Path
import json

from flyin.parser import Parser


class Data():

    key1: int = 42
    key2: int = 16
    key3: str = "toto"

    data_directory: str = "data/"
    data_file_name: str = ""
    data_dict: dict[str, Any] = {}

    def __init__(self) -> None:
        cls = type(self)
        self.nb_drones: int = 1
        self.start_hub: Zone

    @classmethod
    def read_file(cls) -> bool:
        if cls.file_from_argv():
            try:
                with open(cls.data_file_name, "r") as json_file:
                    data_json: str = ""
                    line: str = ""
                    line = json_file.readline()
                    while line:
                        if not line.strip().startswith(("#", "//")):
                            json += line
                        line = json_file.readline()
                    cls.data_dict = json.loads(data_json)
                    cls.set_values(cls.data_dict)
            except FileNotFoundError:
                Error("[error]No data file found.")
            except json.decoder.JSONDecodeError:
                Error("[error]JSON data file corrupted.")
        return (cls.data_dict != {})

    @classmethod
    def write_file(cls) -> None:
        if cls.data_file_name == "" and not cls.file_from_argv():
            cls.data_file_name = "data.json"
        try:
            with open(cls.data_file_name, "w") as data_file:
                data_json: dict[str, Any] = cls.data_dict
                json.dump(data_json, data_file, indent=4)
        except Exception as e:
            Error(f"[error]{e}")

    @classmethod
    def file_from_argv(cls) -> bool:
        try:
            with open(sys.argv[1], "r"):
                cls.data_file_name = sys.argv[1]
        except IndexError:
            Error("[error]No data file provide. "
                  f"Usage: {sys.argv[0].rpartition("/")[2]} <data_file>. ")
        except FileNotFoundError:
            Error(f"[error]Data file <{Parser.argv[1]}> not found. "
                  f"Usage: {sys.argv[0].rpartition("/")[2]} <data_file>. ")
        return (cls.data_file_name != "")

    @classmethod
    def set_values(cls) -> None:
        value_set: bool = False
        for data_key, data_value in cls.data_dict.items():
            try:
                if hasattr(cls, data_key):
                    key_type: type = type(getattr(cls, data_key))
                    if isinstance(data_value, key_type):
                        if cls.verify_value(data_key, data_value):
                            setattr(cls, data_key, data_value)
                            value_set = True
                        else:
                            raise DataValueError(data_key, data_value)
                    else:
                        raise DataTypeError(data_key, data_value, key_type)
                else:
                    raise DataKeyError(data_key)
            except Error:
                pass
        return (value_set)

    @classmethod
    def verify_value(cls, key: str, value: Any) -> bool:
        value_ok: bool = True
        try:
            match key:
                case "key1":
                    if value < 0:
                        raise DataError()

                case "key2":
                    if value < 0:
                        raise DataError()

                case "key3":
                    if value != "toto":
                        raise DataError()
                case _:
                    value_ok = False
        except Error:
            value_ok = False
        return (value_ok)
