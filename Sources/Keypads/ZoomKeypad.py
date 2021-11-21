import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

class ZoomKeypad():
    def __init__(self, colour, keyboard, layout, consumer_control):
        self.colour = colour
        self._keyboard = keyboard
        self._layout = layout
        self._consumer_control = consumer_control
        self.keys = {
                        0: None, 1: None,  2: None, 3: None,
                        4: None, 5: None,  6: None, 7: None,
                        8: None, 9: None,  10: None, 11: None,
                        12: self.key12_pressed, 13: None,  14: self.key14_pressed, 15: self.key15_pressed
                    }

    def key0_pressed(self):
        print('Key 0 press not implemented.')
        
    def key1_pressed(self):
        print('Key 1 press not implemented.')
        
    def key2_pressed(self):
        print('Key 2 press not implemented.')
        
    def key3_pressed(self):
        print('Key 3 press not implemented.')
        
    def key4_pressed(self):
        print('Key 4 press not implemented.')
        
    def key5_pressed(self):
        print('Key 5 press not implemented.')
        
    def key6_pressed(self):
        print('Key 6 press not implemented.')
        
    def key7_pressed(self):
        print('Key 7 press not implemented.')
        
    def key8_pressed(self):
        print('Key 8 press not implemented.')
        
    def key9_pressed(self):
        print('Key 9 press not implemented.')
        
    def key10_pressed(self):
        print('Key 10 press not implemented.')
        
    def key11_pressed(self):
        print('Key 11 press not implemented.')
        
    def key12_pressed(self):
        print('Leaving meeting')
        self._keyboard.send(Keycode.COMMAND, Keycode.W)
        
    def key13_pressed(self):
        print('Key 13 press not implemented.')
        
    def key14_pressed(self):
        print('Start / Stop Video')
        self._keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.V)
        
    def key15_pressed(self):
        print('Mute / Unmute')
        self._keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)
        
    def key_pressed(self, number):
        if number in self.keys:
            self.keys[number]()
        else:
            print(f'Unknown key {number}')