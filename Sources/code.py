import time

from keybow2040 import Keybow2040
from keybow_hardware.pim56x import PIM56X as Hardware # for Keybow 2040

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from Keypads import WildernessLabsKeypad
from Keypads import ZoomKeypad

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Set up consumer control (used to send media key presses)
consumer_control = ConsumerControl(usb_hid.devices)

keybow = Keybow2040(Hardware())
keys = keybow.keys

keybow.set_all(0, 0, 0)

modifier_key_number = 0
modifier_key_rgb = (0, 50, 0)

keypads = {
            1: WildernessLabsKeypad.WildernessLabsKeypad((0, 0, 50), keyboard, layout, consumer_control),
            2: ZoomKeypad.ZoomKeypad((50, 0, 0), keyboard, layout, consumer_control)
          }
current_keypad = keypads[1]

def set_keypad_leds():
    keybow.set_all(0, 0, 0)
    for k in current_keypad.keys:
        if current_keypad.keys[k] is not None:
            keys[k].set_led(*current_keypad.colour)
    keys[0].set_led(*modifier_key_rgb)

@keybow.on_hold(keys[0])
def hold_handler(key):
    keybow.set_all(0, 0, 0)
    for kp in range(1, 16):
        if (kp in keypads):
            keys[kp].set_led(*keypads[kp].colour)
    keys[0].set_led(*modifier_key_rgb)

for key in keys:
    @keybow.on_release(key)
    def release_handler(key):
        global current_keypad
        if key.number == modifier_key_number:
            keybow.set_all(0, 0, 0)
            set_keypad_leds()
        else:
            if keys[modifier_key_number].pressed:
                if key.number in keypads:
                    current_keypad = keypads[key.number]
            else:
                if current_keypad.keys[key.number] is not None:
                    current_keypad.key_pressed(key.number)
                else:
                    print(f'Invalid key {key.number} released')

set_keypad_leds()

keys[0].set_led(*modifier_key_rgb)
while True:
    keybow.update()
