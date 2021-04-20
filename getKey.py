from pynput.keyboard import Controller, Listener

class KeyGetter:
    def __init__(self):
        self._keyboard = Controller()

    def _on_press(self, key):
        print(f"Pressed {key}")
    
    def _on_release(self, key):
        pass
        
    def start(self):
        with Listener(
            on_press=self._on_press,
            on_release=self._on_release) as listener:
            listener.join()
            

if __name__ == "__main__":
    keyGetter = KeyGetter()
    keyGetter.start()