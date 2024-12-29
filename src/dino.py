""" This module contains the behaviour of the dino.
The dino is the main character of the game and is controlled by the player.
It can run, jump and sneak.
classes:
    Dino: This class contains the behaviour of the dino.
    Status: This class contains the status of the dino as an enum.
"""

# pylint: disable=no-member

from enum import Enum
from typing import Final

import pygame as pg

from obstacles import GameElement
from recourses import load_image, seperate_images
from counter import Counter


class Status(Enum):
    """This class contains the status of the dino.
    The status displays the current state of the dino.
    Atributes:
        RUNNING: The dino is running.
        JUMPING: The dino is jumping.
        SNEAKING: The dino is sneaking.
    """

    RUNNING = 1
    JUMPING = 2
    SNEAKING = 3


class Dino(GameElement):
    """This class contains the behaviour of the dino.
    The dino is the main character of the game and is controlled by the player.
    It can run, jump and sneak.
    Atributes:
        position: The vertical position of the dino.
        status: The status of the dino as an enum of the Status class.
        color_theme: The color theme of the dino as a string.

    Methods:
        update: calls the specific method for the current state of the dino.
        check_collision: checks if the dino collides with an object.
    """

    def __init__(self) -> None:
        super().__init__(200, 200)
        self.counter: Counter = Counter()
        self.status: Status = Status.RUNNING

        self.running_image: tuple[list[pg.Surface], pg.Rect]
        self.sneaking_image: tuple[list[pg.Surface], pg.Rect]
        self.load_images()

    def process_input(self, event: pg.event.Event) -> None:
        """This function gets the input from the user.
        It gets all inputs from the previous frame and
        looks for keys they are relevant for the dino movement.
        In case of those keys being pressed, it is checked if it's
        possible to change the state of the dino to the desired one.

        Args:
            event: The event that was triggered by the user

        Variables:
            JUMP_KEYS: list of integers that represent
            the keys that make the dino jump.
            SNEAK_KEYS: list of integers that represent
            the keys that make the dino sneak.

        Examples:
            >>> dino: Dino = Dino()
            >>> for event in pg.event.get():
            >>>     dino.process_input(event)
        """
        JUMP_KEYS: Final[list[int]] = [  # pylint: disable=invalid-name
            pg.K_UP,
            pg.K_SPACE,
        ]
        SNEAK_KEYS: Final[list[int]] = [pg.K_DOWN]  # pylint: disable=invalid-name

        if event.type == pg.KEYDOWN:
            if event.key in JUMP_KEYS and self.status == Status.RUNNING:
                self.status = Status.JUMPING
            if event.key in SNEAK_KEYS and self.status == Status.RUNNING:
                self.status = Status.SNEAKING
        if event.type == pg.KEYUP:
            if event.key in SNEAK_KEYS and self.status == Status.SNEAKING:
                self.status = Status.RUNNING

    def _run(self) -> None:
        """Set the Dino's image to the running image.

        The Dino has two images for running. To create a running animation
        the Dino changes between the two images every 20 frames.
        """
        self.rect = self.running_image[1]
        if self.counter.dino_running_status:
            self.current_image = self.running_image[0][2]
        else:
            self.current_image = self.running_image[0][3]

    def _jump(self) -> None:
        """Set the Dino's image to the jumping image."""
        self.rect = self.running_image[1]
        self.current_image = self.running_image[0][0]

    def _sneak(self) -> None:
        """Set the Dino's image to the sneaking image.

        The Dino has two images for sneaking. To create a sneaking animation
        the Dino changes between the two images every 20 frames.
        """
        self.rect = self.sneaking_image[1]
        if self.counter.dino_running_status:
            self.current_image = self.sneaking_image[0][0]
        else:
            self.current_image = self.sneaking_image[0][1]

    def check_collision(self) -> bool:
        """This function checks if the dino collides with an object."""
        raise NotImplementedError(
            "Subclasses must implement the check_collision method."
        )

    def load_images(self) -> None:
        """This function loads the images for the dino."""
        self.running_image = seperate_images(load_image("dino_running.png")[0], (5, 1))
        self.sneaking_image = seperate_images(
            load_image("dino_sneaking.png")[0], (2, 1)
        )

    def update(self, speed: float = 0) -> None:
        if self.status == Status.RUNNING:
            self._run()
        if self.status == Status.JUMPING:
            self._jump()
        if self.status == Status.SNEAKING:
            self._sneak()
        super().update(speed)
