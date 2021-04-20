import pygame
from pynput.keyboard import Controller


class Utils:
    pygame.init()
    pygame.mixer.init()
    _keyboard = Controller()

    @staticmethod
    def play_sound(path):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(0.15)
        sound.play()

    @staticmethod
    def press_key(key):
        Utils._keyboard.press(key)
        Utils._keyboard.release(key)
