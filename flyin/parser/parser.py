#!/usr/bin/env python3

from __future__ import annotations
from typing import Any
import sys
from pathlib import Path
import json

from flyin.zone import Zone, ZoneType, HubType, Color
from flyin.connection import Connection
from flyin.error import Error, MapFileNotFoundError, NoMapFileProvideError, \
    DataTypeError, DataKeyError, DataValueError, DataError, \
    ParserError, ParametersValueError, NbDroneError, StartHubExistError, EndHubExistError, \
    DashOrSpaceInZoneNameError, CoordMustBeIntegerError, ZoneExistError, \
    ZoneTypeError, NotValidColorError, ZoneNotExistError, SameZoneError


class Parser():

    data_directory: str = "data/"
    verify_func: dict[str, callable] = {}

    def __init__(self) -> None:
        cls = type(self)
        cls.verify_func = {
            "nb_drones": cls.verify_drone,
            "start_hub": cls.verify_hub,
            "end_hub": cls.verify_hub,
            "hub": cls.verify_hub,
            "connection": cls.verify_connection
            }
        cls.read_file()
        if getattr(sys, "frozen", False):
            # Exécution depuis un exécutable PyInstaller
            cls.data_directory = str(
                Path(getattr(sys, "_MEIPASS",
                             Path(__file__).resolve().parent)))\
                                + "/" + cls.data_directory

    @classmethod
    def read_file(cls) -> None:
        # cls.file_from_argv()
        try:
            with open(sys.argv[1], "r") as map_file:
                num_line: int = 1
                line: str = map_file.readline()
                while line:
                    if not line.strip().startswith(("#", "//")) \
                            and line != "\n":
                        data = line.strip().split(":", maxsplit=1)
                        cls.verify_func[data[0]](data)
                    line = map_file.readline()
                    num_line += 1
        except IndexError:
            NoMapFileProvideError().print_and_exit()
        except FileNotFoundError:
            MapFileNotFoundError(sys.argv[1]).print_and_exit()
        except KeyError:
            ParserError(num_line, ParametersValueError(data[0])).print_and_exit()
        except Error as e:
            ParserError(num_line, e).print_and_exit()

    @classmethod
    def verify_drone(cls, data: list[str]) -> None:
        try:
            Zone.nb_drones = int(data[1].strip())
            if Zone.nb_drones < 1:
                raise NbDroneError()
        except ValueError:
            raise NbDroneError()

    @classmethod
    def verify_hub(cls, data: list[str]) -> None:
        hub: HubType = HubType(data[0])
        if hub is HubType.START and Zone.start_hub != "":
            raise StartHubExistError()
        if hub is HubType.END and Zone.end_hub != "":
            raise EndHubExistError()
        param: list[str] = data[1].split()
        name: str = str(param[0])
        if name.find("-") != -1 or name.find(" ") != -1:
            raise DashOrSpaceInZoneNameError(name)
        if name in Zone.hubs:
            raise ZoneExistError(name)
        try:
            xy: tuple[int, int] = (int(param[1]), int(param[2]))
        except ValueError:
            raise CoordMustBeIntegerError()
        meta: dict[str, Any] = {
            "zone": ZoneType.NORMAL,
            "color": Color.NONE,
            "max_drones": 1}
        if len(param) > 3:
            for m in param[3:]:
                key, value = tuple(m.strip("[]").split("=", maxsplit=1))
                if key == "zone":
                    try:
                        meta[key] = ZoneType(value)
                    except:
                        raise ZoneTypeError(value)
                elif key == "color":
                    try:
                        meta[key] = Color(value)
                    except ValueError:
                        raise NotValidColorError(value)
                elif key == "max_drones":
                    if hub not in [HubType.START, HubType.END]:
                        try:
                            meta[key] = int(value)
                            if meta[key] < 1:
                                raise NbDroneError()
                        except ValueError:
                            raise NbDroneError()
                else:
                    raise ParametersValueError(key)
        Zone(hub, name, xy, meta)

    @classmethod
    def verify_connection(cls, data: list[str]) -> None:
        param: list[str] = data[1].split()
        z1, z2 = tuple(param[0].split("-", maxsplit=1))
        if z1 == z2:
            raise SameZoneError()
        try:
            zone1: Zone = Zone.hubs[z1]
        except KeyError:
            raise ZoneNotExistError(z1)
        try:
            zone2: Zone = Zone.hubs[z2]
        except KeyError:
            raise ZoneNotExistError(z2)
        meta: dict[str, int] = {"max_link_capacity": 1}
        if len(param) > 1:
            for p in param[1:]:
                key, value = tuple(p.strip("[]").split("=", maxsplit=1))
                if key == "max_link_capacity":
                    try:
                        meta[key] = int(value)
                        if meta[key] < 1:
                            raise NbDroneError()
                    except ValueError:
                        raise NbDroneError()
                else:
                    raise ParametersValueError(key)
        Connection(zone1, zone2, meta)
