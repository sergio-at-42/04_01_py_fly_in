from __future__ import annotations
from flyin.zone import Zone


class Connection():

    network: dict[tuple[str, str], Connection] = {}

    def __init__(self,
                 zone1: Zone,
                 zone2: Zone,
                 meta: dict[str, int] = {"max_link_capacity": 1}
                ) -> None:
        self.zone1: Zone = zone1
        self.zone2: Zone = zone2
        self.name: str = f"{self.zone1.name}-{self.zone2.name}"
        self.meta: dict[str, int] = meta

    @classmethod
    def add(cls,
            zone1: Zone,
            zone2: Zone,
            meta: dict[str, int] = {"max_link_capacity": 1}
            ) -> None:
        from flyin.link import Link
        new_c: Connection = Connection(zone1, zone2, meta)
        Connection.network[(new_c.zone1.name, new_c.zone2.name)] = new_c
        new_c.zone1.connect.append(Link(new_c.zone2, new_c))
        new_c.zone2.connect.append(Link(new_c.zone1, new_c))
