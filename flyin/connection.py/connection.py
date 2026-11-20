from __future__ import annotations
from typing import Any
from flyin.zone import Zone

class Connection():

    def __init__(self) -> None:
        self.zone1: Zone = Zone()
        self.zone2: Zone = Zone()
        self.meta: dict[str, int] = {"max_link_capacity": 1}

    def name(self) -> str:
        return (f"{self.zone1.name}-{self.zone2.name}")

