from __future__ import annotations
from typing import Any
from .zone_type import ZoneType
from .hub_type import HubType
from .color import Color


class Zone():

    start_hub: Zone = None
    end_hub: Zone = None
    hubs: dict[str, Zone] = {}

    def __init__(self,
                 hub: HubType,
                 name: str,
                 xy: tuple[int, int] = (0, 0),
                zone_type: ZoneType = ZoneType.NORMAL,
                color: Color = Color.NONE,
                max_drones: int = 1
                ) -> None:
        from flyin.drone import Drone
        from flyin.link import Link
        self.hub: HubType = hub
        self.name: str = name
        self.xy: tuple[int, int] = xy
        self.zone_type: ZoneType = zone_type
        self.color: Color = color
        self.max_drones: int = max_drones
        match self.hub:
            case HubType.START:
                self.max_drones = -1
                Zone.start_hub = self
            case HubType.END:
                self.max_drones = -1
                Zone.end_hub = self
        self.connect: list[Link] = []
        self.drones: list[Drone] = []
        Zone.hubs[self.name] = self
