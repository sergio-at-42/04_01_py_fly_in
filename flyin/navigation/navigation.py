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
            if d.pos != Zone.end_hub:
                d.move(cls.path_finding(d).to)
        cls.display_drones_positions()

    @classmethod
    def path_finding(cls, drone: Drone, target: Zone | None = None) -> Link:
        if target is None:
            target = Zone.end_hub
        # pos: Zone = drone.pos 
        search_zones: set[Zone] = set()
        next_zone: Zone = drone.pos # type: ignore
        next_path: Zone = drone.pos # type: ignore
        # next_link: Link = Link(pos, Connection(pos, pos))
        # search_path: list[tuple[Zone, Link]] = []

        # search_link: Link = Link(pos, Connection(pos, pos))
        # search_path: list[tuple[Link, Link]] = []

        visited_zones: set[Zone] = drone.histo_visited.copy()

        for z in drone.pos.connect: # type: ignore
            if z.to == target:
                next_zone = z.to
            elif z.to not in visited_zones and len(z.to.drones) < z.to.max_drones:
                search_zones.add(z.to)


        # next_link: Link = l # type: ignore

        while len(search_zones) > 0 and next_zone != target:
            print("visited ==> ", [z.name for z in zones_visited]) ###################################
            print([(z.name, l.to.name) for z, l in search_path]) #########################################

            z = search_zones.pop()

            print(search_zone.name, next_link.to.name, " | ") ############################################

            if z != target:
                if search_zone not in zones_visited and len(search_zone.drones) < search_zone.max_drones:
                    zones_visited.add(search_zone)
                    for l in search_zone.connect:
                        search_path.append((l.to, next_link))
        
        print(drone.id) ##########################################3333
        # if search_zone != target:
        #     next_link = Link(pos, Connection(pos, pos))
        if next_link.to.name == "dead_end":
            exit(24)
        return (next_link)

    @classmethod
    def display_drones_positions(cls) -> None:
        if len(Drone.fleet) < 1:
            print(">>>>>>   Fleet is empty   <<<<<<")
        else:
            for d in Drone.fleet:
                print(f"{d.id}-", end="")
                print(d.pos.color.ascii(), end="") # type: ignore
                print(f"{d.pos.name}", end="") # type: ignore
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






    # @classmethod
    # def path_finding(cls, drone: Drone, target: Zone | None = None) -> Link:
    #     if target is None:
    #         target = Zone.end_hub
    #     pos: Zone = drone.pos # type: ignore
    #     search_zone: Zone = pos
    #     next_link: Link = Link(pos, Connection(pos, pos))
    #     search_path: list[tuple[Zone, Link]] = []

    #     # search_link: Link = Link(pos, Connection(pos, pos))
    #     # search_path: list[tuple[Link, Link]] = []

    #     zones_visited: set[Zone] = drone.histo_visited.copy()

    #     for l in pos.connect:
    #         if l.to == target:
    #             search_zone = target # type: ignore
    #             next_link = l
    #         elif l.to not in zones_visited and len(l.to.drones) < l.to.max_drones:
    #             search_path.append((pos, l))


    #     # next_link: Link = l # type: ignore

    #     while len(search_path) > 0 and search_zone != target:
    #         print("visited ==> ", [z.name for z in zones_visited]) ###################################
    #         print([(z.name, l.to.name) for z, l in search_path]) #########################################
    #         search_zone, next_link = search_path.pop()
    #         print(search_zone.name, next_link.to.name, " | ") ############################################
    #         if search_zone != target:
    #             if search_zone not in zones_visited and len(search_zone.drones) < search_zone.max_drones:
    #                 zones_visited.add(search_zone)
    #                 for l in search_zone.connect:
    #                     search_path.append((l.to, next_link))
        
    #     print(drone.id) ##########################################3333
    #     # if search_zone != target:
    #     #     next_link = Link(pos, Connection(pos, pos))
    #     if next_link.to.name == "dead_end":
    #         exit(24)
    #     return (next_link)