from configparser import ConfigParser

import pygame
from pynput.keyboard import Controller
from os import path


class Utils:
    pygame.init()
    pygame.mixer.init()
    _keyboard = Controller()

    @staticmethod
    def play_sound(filepath):
        sound = pygame.mixer.Sound(filepath)
        sound.set_volume(0.15)
        sound.play()

    @staticmethod
    def press_key(key):
        Utils._keyboard.press(key)
        Utils._keyboard.release(key)

    @staticmethod
    def load_ini_file(filename: str):
        if filename[-4:].lower() != ".ini":
            filename += ".ini"

        if not path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' was not found")

        config = ConfigParser()
        config.read(filename)
        return config
