from __future__ import annotations
from flyin.zone import Zone


class Drone():

    nb_drones: int = 1
    nb_id: int = 0
    fleet: list[Drone] = []

    def __init__(self, pos: Zone | None = None) -> None:
        Drone.nb_id += 1
        self.id: str = f"D{Drone.nb_id}"
        self.pos: Zone = pos
        if self.pos is None:
            self.pos = Zone.start_hub
        self.pos.drones.append(self)
        Drone.fleet.append(self)

    @classmethod
    def reset(cls) -> None:
        cls.fleet.clear()
        for _ in range(cls.nb_drones):
            Drone()

    def move(self, pos: Zone) -> None:
        self.pos.drones.remove(self)
        self.pos = pos
        self.pos.drones.append(self)