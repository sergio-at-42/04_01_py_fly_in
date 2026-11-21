from enum import Enum


class HubType(Enum):
    HUB = "hub"
    START = "start_hub"
    END = "end_hub"

    def bit(self) -> int:
        bit_value: 0
        match self.value:
            case "hub":
                bit_value = 1
            case "start_hub":
                bit_value = 2
            case "end_hub":
                bit_value = 4
        return (bit_value)
