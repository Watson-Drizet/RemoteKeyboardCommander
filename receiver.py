from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pynput.keyboard import Key, Controller
import time
import os
pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-dd5c661f-ba65-4081-815a-04dc3eac0296'
pnconfig.subscribe_key = 'sub-c-4f073e42-a145-11eb-8d7b-b642bba3de20'
pnconfig.ssl = True
pubnub = PubNub(pnconfig)
keyboard = Controller()

INTERACT = 'f'

def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass
        
def press(key):
    keyboard.press(key)
    keyboard.release(key)
    
class MySubscribeCallback(SubscribeCallback):
    msg = ""
    def presence(self, pubnub, presence):
        pass
    def status(self, pubnub, status):
        pass
    def message(self, pubnub, message):
        MySubscribeCallback.msg = message.message
        #print("from device 1: " + message.message)

    @staticmethod
    def get_msg_and_empty():
        result = MySubscribeCallback.msg
        MySubscribeCallback.msg = ""
        return result
        
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()
## publish a message
while True:
    pubnub.publish().channel("chan-1").pn_async(my_publish_callback)
    msg = MySubscribeCallback.get_msg_and_empty()
    if msg != "":
        if msg == "enter":
            press(Key.enter)
            print("Pressed enter")
        elif msg == "interact":
            press(INTERACT)
            print(f"Pressed {INTERACT}")
        elif len(msg) == 1 and (msg[0].isalpha() or msg[0].isdigit()):
            keyboard.press(msg)
            keyboard.release(msg)
            print(f"{msg}")
        else:
            print(f"unknown msg type: {msg}")

