from __future__ import annotations

from flyin.drone import Drone
from flyin.zone import Zone, ZoneType, HubType, Color
from flyin.connection import Connection
from flyin.link import Link


class Navigation():

    nb_turn: int = 0

    def __init__(self) -> None:
        cls = type(self)
        print()
        cls.display_drones_positions()
        while Zone.end_hub is not None \
                and len(Zone.end_hub.drones) < Drone.nb_drones:
            cls.next_turn()
        print()
        cls.print_result()
        print()

    @classmethod
    def next_turn(cls) -> None:
        cls.nb_turn += 1
        for d in Drone.fleet:
            d.move(cls.path_finding(d).to)
        cls.display_drones_positions()

    @classmethod
    def path_finding(cls, drone: Drone, target: Zone | None = None) -> Link:
        if target is None:
            target = Zone.end_hub
        pos: Zone = drone.pos
        search_zone: Zone = pos
        next_link: Link = Link(pos, Connection(pos, pos))
        search_path: list[tuple[Zone, Link]] = []
        zones_visited: list[Zone] = []

        for l in pos.connect:
            if len(l.to.drones) < l.to.max_drones:
                search_path.append((pos, l))
            elif l.to == target:
                search_path.append((pos, l))

        while len(search_path) > 0 and search_zone != target:
            search_zone, next_link = search_path.pop()
            if search_zone != target:
                if search_zone not in zones_visited:
                    zones_visited.append(search_zone)
                    for l in search_zone.connect:
                        search_path.append((l.to, next_link))
        return (next_link)

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
    def print_result(cls) -> None:
        msg: str = f">>>   {cls.nb_turn}   <<<"
        spc: str = " " * ((80 - len(msg)) // 2)
        msg: str = spc + msg + spc
        # empty_line: str = "".ljust(len(msg))
        score: str = "SCORE   SCORE   SCORE   SCORE   SCORE   SCORE"
        best: str = "THIS IS THE BEST CODE I HAVE NEVER SEEN BEFORE"
        print(Color.NONE.ascii(), Color.BGCYAN.ascii(), Color.BLUE.ascii(), Color.DIMMED.ascii(), Color.BLINKING.ascii(), sep="", end="")
        print(score.rjust((len(msg) + len(score)) // 2).ljust(len(msg)))
        # print(empty_line)
        print(Color.NONE.ascii(), Color.BGBLUE.ascii(), Color.CYAN.ascii(), sep="", end="")
        # print(empty_line)
        print(msg)
        # print(empty_line)
        print(Color.NONE.ascii(), Color.BGCYAN.ascii(), Color.BLUE.ascii(), Color.DIMMED.ascii(), Color.BLINKING.ascii(), sep="", end="")
        # print(empty_line)
        print(best.rjust((len(msg) + len(best)) // 2).ljust(len(msg)))
        print(Color.NONE.ascii(), sep="", end="")
