from __future__ import annotations
from flyin.drone import Drone
from flyin.zone import Color


class DisplayTerm():

    @classmethod
    def display_drones_positions(cls) -> None:
        if len(Drone.fleet) < 1:
            print(">>>>>>   Fleet is empty   <<<<<<")
        else:
            for d in Drone.fleet:
                print(f"{d.id}-", end="")
                print(d.pos.color.ascii(), end="") # type: ignore
                print(f"{d.pos.name}", end="") # type: ignore
                print(Color.NONE.ascii(), end=" ")
            print()

    @classmethod
    def print_result(cls) -> None:
        from flyin.navigation import Navigation
        msg: str = f">>>   {Navigation.nb_turn}   <<<"
        spc: str = " " * ((80 - len(msg)) // 2)
        msg: str = spc + msg + spc
        # empty_line: str = "".ljust(len(msg))
        score: str = "SCORE   SCORE   SCORE   SCORE   SCORE   SCORE"
        best: str = "THIS IS THE BEST CODE I HAVE NEVER SEEN BEFORE"
        print(Color.NONE.ascii(), Color.BGCYAN.ascii(), Color.BLUE.ascii(), Color.DIMMED.ascii(), Color.BLINKING.ascii(), sep="", end="")
        print(score.rjust((len(msg) + len(score)) // 2).ljust(len(msg)))
        # print(empty_line)
        print(Color.NONE.ascii(), Color.BGBLUE.ascii(), Color.CYAN.ascii(), sep="", end="")
        # print(empty_line)
        print(msg)
        # print(empty_line)
        print(Color.NONE.ascii(), Color.BGCYAN.ascii(), Color.BLUE.ascii(), Color.DIMMED.ascii(), Color.BLINKING.ascii(), sep="", end="")
        # print(empty_line)
        print(best.rjust((len(msg) + len(best)) // 2).ljust(len(msg)))
        print(Color.NONE.ascii(), sep="", end="")
        print()
