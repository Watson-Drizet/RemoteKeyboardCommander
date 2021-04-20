from threading import Thread

from inner.pubNubManager import PubNubManager
from inner.utils import Utils
from settings import keys


class Receiver(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True

    def run(self):
        while self.running:
            message = PubNubManager.receive()

            if message is not None:
                if message in keys.RECEIVER_KEYS:
                    receiver_key = keys.RECEIVER_KEYS[message]
                    Utils.press_key(receiver_key)
                    print(f"Pressing {receiver_key}")
                else:
                    print(f"Received unknown message: {message}")

    def stop(self):
        self.running = False


if __name__ == "__main__":
    receiver = Receiver()
    receiver.run()
