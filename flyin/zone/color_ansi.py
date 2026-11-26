
ANSI_COLORS: dict[str, str] = {
    # Couleurs standard (0-7)
    "black": "\033[38;5;0m",
    "red": "\033[38;5;1m",
    "green": "\033[38;5;2m",
    "yellow": "\033[38;5;3m",
    "blue": "\033[38;5;4m",
    "magenta": "\033[38;5;5m",
    "cyan": "\033[38;5;6m",
    "white": "\033[38;5;7m",

    # Couleurs haute intensité (8-15)
    "bright_black": "\033[38;5;8m",
    "bright_red": "\033[38;5;9m",
    "bright_green": "\033[38;5;10m",
    "bright_yellow": "\033[38;5;11m",
    "bright_blue": "\033[38;5;12m",
    "bright_magenta": "\033[38;5;13m",
    "bright_cyan": "\033[38;5;14m",
    "bright_white": "\033[38;5;15m",

    # Palette de gris (232-255)
    "gray_0": "\033[38;5;232m",
    "gray_1": "\033[38;5;233m",
    "gray_2": "\033[38;5;234m",
    "gray_3": "\033[38;5;235m",
    "gray_4": "\033[38;5;236m",
    "gray_5": "\033[38;5;237m",
    "gray_6": "\033[38;5;238m",
    "gray_7": "\033[38;5;239m",
    "gray_8": "\033[38;5;240m",
    "gray_9": "\033[38;5;241m",
    "gray_10": "\033[38;5;242m",
    "gray_11": "\033[38;5;243m",
    "gray_12": "\033[38;5;244m",
    "gray_13": "\033[38;5;245m",
    "gray_14": "\033[38;5;246m",
    "gray_15": "\033[38;5;247m",
    "gray_16": "\033[38;5;248m",
    "gray_17": "\033[38;5;249m",
    "gray_18": "\033[38;5;250m",
    "gray_19": "\033[38;5;251m",
    "gray_20": "\033[38;5;252m",
    "gray_21": "\033[38;5;253m",
    "gray_22": "\033[38;5;254m",
    "gray_23": "\033[38;5;255m",
}

# Génération automatique des 216 couleurs RGB (16-231)
# et des noms génériques color_16 à color_231.
ANSI_COLORS.update({
    f"color_{i}": f"\033[38;5;{i}m"
    for i in range(16, 232)
})

RESET = "\033[0m"
