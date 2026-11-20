#!/usr/bin/env python3

from flyin import *


class Flyin():
    def __init__(self) -> None:
        Error.log_application_started()

        Error.log_game_over()
        print(Error.read_log())


if __name__ == "__main__":
    Flyin()
