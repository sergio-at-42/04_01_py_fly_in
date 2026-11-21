from __future__ import annotations
from flyin.zone import Zone


class Connection():

    connections: dict[tuple[str, str], Connection] = {}

    def __init__(self,
                 zone1: Zone,
                 zone2: Zone,
                 meta: dict[str, int] = {"max_link_capacity": 1}
                ) -> None:
        self.zone1: Zone = zone1
        self.zone2: Zone = zone2
        self.meta: dict[str, int] = meta
        Connection.connections[(self.zone1.name, self.zone2.name)] = self

    def name(self) -> str:
        return (f"{self.zone1.name}-{self.zone2.name}")
