from pynput.keyboard import Listener

from inner.pubNubManager import PubNubManager
from inner.utils import Utils
from receiver import Receiver
from settings import keys


class Sender:
    def __init__(self):
        self._enabled = True

    def _on_press(self, key):
        pass

    def _on_release(self, key):
        print(f"Pressed {key}")

        if key == keys.SENDER_TOGGLE:
            self._enabled = not self._enabled
            if self._enabled:
                Utils.play_sound("audio/enable.wav")
            else:
                Utils.play_sound("audio/disable.wav")
            print(f"is enabled:{self._enabled}")

        elif self._enabled:
            if key in keys.SENDER_KEYS:
                message = keys.SENDER_KEYS.get(key)
                PubNubManager.send(message)

    def start(self):
        with Listener(
                on_press=self._on_press,
                on_release=self._on_release) as listener:
            listener.join()


if __name__ == "__main__":
    receiver = Receiver()
    receiver.start()

    sender = Sender()
    sender.start()
