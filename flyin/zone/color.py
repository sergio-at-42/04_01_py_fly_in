from enum import Enum


class Color(Enum):

    # Reset color
    NONE = "none"
    # Basic colors
    BLACK = "black"
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    MAGENTA = "magenta"
    CYAN = "cyan"
    WHITE = "white"
    ORANGE = "orange"
    PURPLE = "purple"
    BROWN = "brown"
    LIME = "lime"
    GOLD = "gold"
    MAROON = "maroon"
    DARKRED = "darkred"
    VIOLET = "violet"
    CRIMSON = "crimson"
    RAINBOW = "rainbow"
    # Background colors
    BGBLACK = "bgblack"
    BGRED = "bgred"
    BGGREEN = "bggreen"
    BGYELLOW = "bgyellow"
    BGBLUE = "bgblue"
    BGMAGENTA = "bgmagenta"
    BGCYAN = "bgcyan"
    BGWHITE = "bgwhite"
    BGORANGE = "bgorange"
    BGPURPLE = "bgpurple"
    BGBROWN = "bgbrown"
    BGLIME = "bglime"
    BGGOLD = "bggold"
    BGMAROON = "bgmaroon"
    BGDARKRED = "bgdarkred"
    BGVIOLET = "bgviolet"
    BGCRIMSON = "bgcrimson"
    BGRAINBOW = "bgrainbow"

    # Style
    BOLD = "bold"
    DIMMED = "dimmed"
    ITALIC = "italic"
    UNDERLINE = "underline"
    BLINKING = "blinking"
    INVERSION = "inversion"

    # Cursor Mode
    CURSOROFF = "cursoroff"
    CURSORON = "cursoron"

    def ascii(self) -> str:
        ascii_value: str = "\033[0m"
        match self.value:
            case "none":
                ascii_value = "\033[0m"         # Reset
            case "black":
                ascii_value = "\033[30m"        # Black
            case "red":
                ascii_value = "\033[31m"        # Red
            case "green":
                ascii_value = "\033[32m"        # Green
            case "yellow":
                ascii_value = "\033[33m"        # Yellow
            case "blue":
                ascii_value = "\033[34m"        # Blue
            case "magenta":
                ascii_value = "\033[35m"        # Magenta
            case "cyan":
                ascii_value = "\033[36m"        # Cyan
            case "white":
                ascii_value = "\033[37m"        # White
            case "orange":
                ascii_value = "\033[38;5;208m"  # Orange
            case "purple":
                ascii_value = "\033[38;5;5m"    # Purple
            case "brown":
                ascii_value = "\033[38;5;94m"   # Brown
            case "lime":
                ascii_value = "\033[38;5;10m"   # Lime
            case "gold":
                ascii_value = "\033[38;5;220m"  # Gold
            case "maroon":
                ascii_value = "\033[38;5;1m"    # Maroon
            case "darkred":
                ascii_value = "\033[38;5;88m"   # Darkred
            case "violet":
                ascii_value = "\033[38;5;129m"  # Violet
            case "crimson":
                ascii_value = "\033[38;5;161m"  # Crimson
            case "rainbow":
                ascii_value = "\033[38;5;128m"  # Rainbow
            case "bgblack":
                ascii_value = "\033[40m"        # Black
            case "bgred":
                ascii_value = "\033[41m"        # Red
            case "bggreen":
                ascii_value = "\033[42m"        # Green
            case "bgyellow":
                ascii_value = "\033[43m"        # Yellow
            case "bgblue":
                ascii_value = "\033[44m"        # Blue
            case "bgmagenta":
                ascii_value = "\033[45m"        # Magenta
            case "bgcyan":
                ascii_value = "\033[46m"        # Cyan
            case "bgwhite":
                ascii_value = "\033[47m"        # White
            case "bgorange":
                ascii_value = "\033[48;5;208m"  # Orange
            case "bgpurple":
                ascii_value = "\033[48;5;5m"    # Purple
            case "bgbrown":
                ascii_value = "\033[48;5;94m"   # Brown
            case "bglime":
                ascii_value = "\033[48;5;10m"   # Lime
            case "bggold":
                ascii_value = "\033[48;5;220m"  # Gold
            case "bgmaroon":
                ascii_value = "\033[48;5;1m"    # Maroon
            case "bgdarkred":
                ascii_value = "\033[48;5;88m"   # Darkred
            case "bgviolet":
                ascii_value = "\033[48;5;129m"  # Violet
            case "bgcrimson":
                ascii_value = "\033[48;5;161m"  # Crimson
            case "bgrainbow":
                ascii_value = "\033[48;5;128m"  # Rainbow
            case "bold":
                ascii_value = "\033[1m"	        # Bold
            case "dimmed":
                ascii_value = "\033[2m"	        # Dimmed
            case "italic":
                ascii_value = "\033[3m"	        # Italic
            case "underline":
                ascii_value = "\033[4m"         # Underlined
            case "blinking":
                ascii_value = "\033[5m"         # Blinking
            case "inversion":
                ascii_value = "\033[7m"         # Foreground/background inversion
            case "cursoroff":
                ascii_value = "\033[?25l"       # Cusor OFF
            case "cursoron":
                ascii_value = "\033[?25h"       # Cursor ON
        return (ascii_value)

    def print(self) -> None:
        print(self.ascii())
