from __future__ import annotations
from flyin.zone import Zone
from flyin.connection import Connection


class Link():

    def __init__(self, to_zone: Zone, by_connection: Connection) -> None:
        self.to: Zone = to_zone
        self.by: Connection = by_connection
