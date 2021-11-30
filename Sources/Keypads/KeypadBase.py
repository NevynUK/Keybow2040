import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

class KeypadBase():
    def __init__(self, colour, name, keyboard, layout, consumer_control):
        self._colour = colour
        self._keyboard = keyboard
        self._layout = layout
        self._name = name
        self._consumer_control = consumer_control
        self._keys = {
                0: None, 1: None,  2: None, 3: None,
                4: None, 5: None,  6: None, 7: None,
                8: None, 9: None,  10: None, 11: None,
                12: None, 13: None,  14: None, 15: None
            }

    @property
    def name(self):
        return(self._name)

    @property
    def colour(self):
        return(self._colour)

    @property
    def keys(self):
        return(self._keys)

    def send_keystrokes(self, *keycodes: int):
        self._keyboard.send(*keycodes)

    def execute_command(self, command):
        self._layout.write(f'{command}\n')

    def key_pressed(self, number):
        if number in self.keys:
            self.keys[number]()
        else:
            print(f'Unknown key {number}')
