#!/usr/bin/env python3

from __future__ import annotations
from typing import Any
import sys
from pathlib import Path
import json

from flyin.zone import Zone, ZoneType, HubType, Color
from flyin.connection import Connection
from flyin.error import Error, DataTypeError, DataKeyError, DataValueError, DataError, ParametersValueError, NbDroneError, SameZoneError


class Parser():

    key1: int = 42
    key2: int = 16
    key3: str = "toto"

    data_directory: str = "data/"
    data_file_name: str = ""
    data_dict: dict[str, Any] = {}

    def __init__(self) -> None:
        cls = type(self)
        cls.read_file()
        if getattr(sys, "frozen", False):
            # Exécution depuis un exécutable PyInstaller
            cls.data_directory = str(
                Path(getattr(sys, "_MEIPASS",
                             Path(__file__).resolve().parent)))\
                                + "/" + cls.data_directory

    @classmethod
    def read_file(cls) -> bool:
        if cls.file_from_argv():
            try:
                with open(cls.data_file_name, "r") as data_file:
                    num_line: int = 1
                    line: str = data_file.readline()
                    while line:
                        if not line.strip().startswith(("#", "//")) \
                                and line != "\n":
                            cls.set_values(num_line, line)
                        line = data_file.readline()
                        num_line += 1
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
    def set_values(cls, num_line: int, line: str) -> None:
        try:
            data = line.split(":", maxsplit=1)
            print(data)
            if data[0] == "nb_drones":
                cls.verify_drone(data[1])
            elif data[0] in ["start_hub", "end_hub", "hub"]:
                cls.verify_hub(data)
            elif data[0] == "connection":
                cls.verify_connection(data)
            else:
                raise ParametersValueError(data[0])
            # if hasattr(cls, data_key):
            #     key_type: type = type(getattr(cls, data_key))
            #     if isinstance(data_value, key_type):
            #         if cls.verify_value(data_key, data_value):
            #             setattr(cls, data_key, data_value)
            #             value_set = True
            #         else:
            #             raise DataValueError(data_key, data_value)
            #     else:
            #         raise DataTypeError(data_key, data_value, key_type)
            # else:
            #     raise DataKeyError(data_key)
        except Error as e:
            Error(f"Parser Error line {num_line} : {e}").print_and_exit()

    @classmethod
    def verify_drone(cls, nb_drones: str) -> None:
        try:
            Zone.nb_drones = int(nb_drones.strip())
            if Zone.nb_drones < 1:
                raise NbDroneError()
        except ValueError:
            raise NbDroneError()


    @classmethod
    def verify_hub(cls, data: list[str]) -> None:
        try:
            hub: HubType = HubType(data[0])
            param: list[str] = data[1].split()
            name: str = str(param[0])
            xy: tuple[int, int] = (int(param[1]), int(param[2]))
            meta: dict[str, Any] = {
                "zone": ZoneType.NORMAL,
                "color": Color.NONE,
                "max_drones": 1}
            if len(param) == 4:
                for m in param[3].split():
                    key, value = tuple(m.split("=", maxsplit=1))
                    if key == "color":
                        meta[key] = Color(value)
                    elif key == "zone":
                        meta[key] = ZoneType(value)
                    elif key == "max_drones":
                        meta[key] == int(value)
                    else:
                        raise ParametersValueError
            Zone(hub, name, xy, meta)
        
            print(HubType(data[0]))
            print(data[1].split())
        except :
            pass


    @classmethod
    def verify_connection(cls, data: list[str]) -> None:
        try:
            print(data[1].split())
        except:
            pass



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


# 

