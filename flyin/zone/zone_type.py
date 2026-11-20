from enum import Enum


class ZoneType(Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

    def bit(self) -> int:
        bit_value: 0
        match self.value:
            case "normal":
                bit_value = 1
            case "restricted":
                bit_value = 2
            case "blocked":
                bit_value = 4
            case "priority":
                bit_value = 8
        return (bit_value)
