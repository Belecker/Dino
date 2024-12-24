"""This module manages the external resources of the game.
It is responsible for loading and storing the images and sounds from their files and preparing
them for use in the game.
"""
import os
import pygame as pg


def full_path(file_name:str, color_theme:str="") -> str:
    """Return the full path of a file in the recources directory.

    Args:
        color_theme (str): The color theme of the file as a directory.
        file_name (str): The name of the file.
    
    Returns:
        str: The full path of the file.
    """
    if not color_theme:
        # Only executed if it is a sound file
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "sounds", file_name))
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "images", color_theme, file_name))

def load_image(color_theme:str, file_name:str) -> pg.Surface:
    """Load an image from a file and return it as a pygame.Surface object.

    Args:
        file_name (str): The name of the file to load.
        color_theme (str): The color theme of the image.
    
    Returns:
        image (pg.Surface): The loaded image as a pygame.Surface object.
    """
    path: str = full_path(file_name, color_theme)
    try:
        image: pg.Surface = pg.image.load(path).convert_alpha()
    except FileNotFoundError as error:
        raise SystemExit(f"Could not load image '{path}' : {str(error)}") from error

    # Makes the background of the image transparent
    image.set_colorkey(image.get_at((0, 0)))
    return image

def load_sound(file_name:str) -> pg.mixer.Sound:
    """Load a sound from a file and return it as a pygame.mixer.Sound object.

    Args:
        file_name (str): The name of the file to load.
    
    Returns:
        sound (pg.mixer.Sound): The loaded sound as a pygame.mixer.Sound object.
    """
    path: str = full_path(file_name)
    try:
        sound: pg.mixer.Sound = pg.mixer.Sound(path)
    except FileNotFoundError as error:
        raise SystemExit(f"Could not load sound '{path}' : {str(error)}") from error
    return sound

def seperate_images(image: pg.Surface, size: tuple[int, int]) -> list[pg.Surface]:
    """Seperate an image into smaller images of a given size.
    All of them must have the same size and must be ordered in a grid.

    Args:
        image (pg.Surface): The image to seperate.
        size (tuple[int, int]): The amount of the image to seperate. (width, height)
    
    Returns:
        list[pg.Surface]: A list of seperated images.
    """
    width: float = image.get_width() / size[0]
    height: float = image.get_height() / size[1]
    immages: list[pg.Surface] = []

    for i in range(size[1]):
        for j in range(size[0]):
            immages.append(image.subsurface((j * width, i * height, width, height)))
    return immages
