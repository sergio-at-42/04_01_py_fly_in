from __future__ import annotations
from typing import Any
from .zone_type import ZoneType
from .hub_type import HubType
from .color import Color


class Zone():

    start_hub: str = ""
    end_hub: str = ""
    hubs: dict[str, Zone] = {}
    nb_drones: int = 1

    def __init__(self,
                 hub: HubType,
                 name: str,
                 xy: tuple[int, int] = (0, 0),
                 meta: dict[str, Any] = {
                    "zone": ZoneType.NORMAL,
                    "color": Color.NONE,
                    "max_drones": 1}
                ) -> None:
        self.hub: HubType = hub
        self.name: str = name
        self.xy: tuple[int, int] = xy
        self.meta: dict[str, Any] = meta
        match self.hub:
            case HubType.START:
                Zone.start_hub = self.name
            case HubType.END:
                Zone.end_hub = self.name
        Zone.hubs[self.name] = self
