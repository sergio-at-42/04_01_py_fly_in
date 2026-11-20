from __future__ import annotations
from typing import Any
from .zone_type import ZoneType
from .color import Color


class Zone():

    def __init__(self) -> None:
        self.name: str = ""
        self.xy: tuple[int, int] = (0, 0)
        self.meta: dict[str, Any] = {
            "zone": ZoneType.NORMAL,
            "color": Color.NONE,
            "max_drones": 1
        }
