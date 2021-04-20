from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pynput.keyboard import Key, Controller, Listener
import pygame
import time
import os


class Sender:
    _INTERACT = 'f'
    _TOGGLE_KEY = Key.f16
    _ENTER_SENDER = Key.f14
    _INTERACT_SENDER = Key.f15
    
    def __init__(self):
        self._keyboard = Controller()
        pygame.init()
        pygame.mixer.init()
        self._pubnub_init()
        
        self._enabled = True
        
    def _pubnub_init(self):
        pnconfig = PNConfiguration()
        pnconfig.publish_key = 'pub-c-dd5c661f-ba65-4081-815a-04dc3eac0296'
        pnconfig.subscribe_key = 'sub-c-4f073e42-a145-11eb-8d7b-b642bba3de20'
        pnconfig.ssl = True
        self._pubnub = PubNub(pnconfig)
        self._pubnub.add_listener(MySubscribeCallback())
        self._pubnub.subscribe().channels("chan-1").execute()
        
    def _play_sound(self, path):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(0.15)
        sound.play()
        
    def _on_press(self, key):
        print(f"Pressed {key}")
        msg = ""
        if key == self._TOGGLE_KEY:
            self._enabled = not self._enabled
            if self._enabled:
                self._play_sound("audio/enable.wav")
            else:
                self._play_sound("audio/disable.wav")
            print(f"is enabled:{self._enabled}")
        elif self._enabled:
            if key == self._ENTER_SENDER:
                msg = "enter"
                self._press(Key.enter)
            elif key == self._INTERACT_SENDER:
                msg = 'interact'
                self._press(self._INTERACT)
                
            if msg != "":
                self._pubnub.publish().channel("chan-1").message(str(msg)).pn_async(Sender._my_publish_callback)
    
    def _press(self, key):
        self._keyboard.press(key)
        self._keyboard.release(key)
    
    @staticmethod
    def _my_publish_callback(envelope, status):
        # Check whether request successfully completed or not
        if not status.is_error():
            pass

    def _on_release(self, key):
        pass
        
    def start(self):
        with Listener(
            on_press=self._on_press,
            on_release=self._on_release) as listener:
            listener.join()
        

class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass
    def status(self, pubnub, status):
        pass
    def message(self, pubnub, message):
        pass
        #print("from device 2: " + message.message)


if __name__ == "__main__":
    sender = Sender()
    sender.start()