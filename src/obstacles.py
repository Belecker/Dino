"""This modules contains the central GameElement class of the game.
It provides the functionality to create and manage
the basic elements of the game.
"""

import pygame as pg
from recourses import load_image, seperate_images

class GameElement(pg.sprite.Sprite):
    """This class represents any element in the game.
    It is a subclass of the pygame.sprite.Sprite class.
    It has a rect attribute that represents its position and size.
    """
    def __init__(self, x_position:float, y_position:float) -> None:
        super().__init__()
        self.x_position: float = x_position
        self.y_position: float = y_position

class Cactus(GameElement):
    """This class represents a Cactus element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """
    def __init__(self, x_position:float, y_position:float) -> None:
        super().__init__(x_position, y_position)
        self.image_1: tuple[list[pg.Surface], pg.Rect]
        self.image_2: tuple[list[pg.Surface], pg.Rect]
        self.image_1 = seperate_images(load_image("cactus-big.png")[0], (3, 1))
        self.image_2 = seperate_images(load_image("cactus-small.png")[0], (3, 1))
