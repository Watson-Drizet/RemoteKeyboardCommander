from pynput.keyboard import Key

# If you're not sure what the exact name of your key is, run getKey.py and press the key.
# It will print out the key's name


SENDER_TOGGLE = Key.f16

# If a specific key is pressed, it will send its value's command
SENDER_KEYS = {
    Key.f14: "enter",
    Key.f15: "interact"
}

# The dict's key is the received command, the value is the button that should be pressed
RECEIVER_KEYS = {
    "enter": Key.enter,
    "interact": 'f'
}
