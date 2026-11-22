from __future__ import annotations
from typing import Any
import sys
from pathlib import Path

from flyin.drone import Drone
from flyin.zone import Zone, ZoneType, HubType, Color
from flyin.connection import Connection
from flyin.link import Link


class Navigation():

    data_directory: str = "data/"
    verify_func: dict[str, callable] = {}

    nb_turn: int = 0

    def __init__(self) -> None:
        cls = type(self)
        print()
        cls.display_drones_positions()
        while len(Zone.end_hub.drones) < Drone.nb_drones:
            cls.next_turn()
        print()

    @classmethod
    def display_drones_positions(cls) -> None:
        if len(Drone.fleet) < 1:
            print(">>>>>>   Fleet is empty   <<<<<<")
        else:
            for d in Drone.fleet:
                print(f"{d.id}-", end="")
                print(d.pos.color.ascii(), end="")
                print(f"{d.pos.name}", end="")
                print(Color.NONE.ascii(), end=" ")
            print()

    @classmethod
    def next_turn(cls) -> None:
        for d in Drone.fleet:
            d.move(cls.path_finding(d).to)
        cls.display_drones_positions()

    @classmethod
    def path_finding(cls, drone: Drone, target: Zone = None) -> Link:

        if target is None:
            target = Zone.end_hub
        pos: Zone = drone.pos
        search_zone: Zone = pos
        next_link: Link = Link(pos, Connection(pos, pos))
        search_path: list[(Zone, Link)] = []
        zones_visited: list[Zone] = []
        for l in pos.connect:
            search_path.append((pos, l))
        while len(search_path) > 0 and search_zone != target:
            search_zone, next_link = search_path.pop()
            if search_zone != target:
                if search_zone not in zones_visited:
                    zones_visited.append(search_zone)
                    for l in search_zone.connect:
                        search_path.append((l.to, next_link))
        return (next_link)
