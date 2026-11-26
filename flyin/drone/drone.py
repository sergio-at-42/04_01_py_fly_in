from __future__ import annotations
from flyin.zone import Zone


class Drone():

    nb_drones: int = 1
    nb_id: int = 0
    fleet: list[Drone] = []

    def __init__(self, pos: Zone | None = None) -> None:
        Drone.nb_id += 1
        self.id: str = f"D{Drone.nb_id}"
        self.pos: Zone | None = pos
        if self.pos is None:
            self.pos = Zone.start_hub
        self.prev_pos: Zone | None = self.pos
        self.histo_visited: set[Zone] = {self.pos} # type: ignore
        self.pos.drones.append(self) # type: ignore
        Drone.fleet.append(self)

    @classmethod
    def reset(cls) -> None:
        # Initialisation of the fleet only if startup position is defined
        if Zone.start_hub is not None:
            cls.fleet.clear()
            for _ in range(cls.nb_drones):
                Drone()

    def move(self, pos: Zone) -> None:
        for link in self.pos.connect: # type: ignore
            if link.to == pos:
                link.by.drones.add(self) 
        self.pos.drones.remove(self) # type: ignore
        self.prev_pos = self.pos
        self.pos = pos
        self.histo_visited.add(self.pos) # type: ignore
        self.pos.drones.append(self)
