"""The main module contains the main functionality of the programm.
It is the file, meant to be called directly to playthe game.
It initializes the grafics as well as controlls the main game functionalitys
defined in other modules.
"""
# pylint: disable=no-member

from random import randint  # pylint: disable=unused-import
import time as t  # pylint: disable=unused-import
import sys
import pygame as pg
from dino import Dino, Status

pg.init()


# Initializes the window
window_scale: list[int] = [800, 600]
window: pg.Surface = pg.display.set_mode((window_scale[0], window_scale[1]))
pg.display.set_caption("Dino")

dino: Dino = Dino()

# Initializes the colors
black: pg.Color = pg.Color(0, 0, 0)
white: pg.Color = pg.Color(255, 255, 255)
gray: pg.Color = pg.Color(190, 190, 190)

jump_keys: list[int] = [pg.K_UP, pg.K_SPACE]
sneak_keys: list[int] = [pg.K_DOWN]

object_speed: int
score: int = 0


def get_input() ->  None:
    """This function gets the input from the user.
    It collects all inputs from the previous frame and
    processes them by modyfying the game according to the player wishes.
    """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key in jump_keys and dino.status == Status.RUNNING:
                dino.status = Status.JUMPING
            if event.key in sneak_keys and dino.status == Status.RUNNING:
                dino.status = Status.SNEAKING
        if event.type == pg.KEYUP:
            if event.key in sneak_keys and dino.status == Status.SNEAKING:
                dino.status = Status.RUNNING



def game_over() -> None:
    """This function is called when the game is over."""

    sys.exit()
    pg.quit()


def main() -> None:
    """This is the main function of the programm.
    It is the place were every functionality is stticked together.
    It initializes the game, runs it displays changes and checks for kollisiions.
    """

    while True:
        get_input()
        move_objects()
        update_display()

        if kollision():
            break
        count_score()

    game_over()


if __name__ == "__main__":
    main()
