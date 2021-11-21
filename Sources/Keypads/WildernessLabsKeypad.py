import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

class WildernessLabsKeypad():
    def __init__(self, colour, keyboard, layout, consumer_control):
        self.colour = colour
        self._keyboard = keyboard
        self._layout = layout
        self._consumer_control = consumer_control
        self.keys = {
                        0: None, 1: self.key1_pressed,  2: self.key2_pressed, 3: self.key3_pressed,
                        4: None, 5: None,  6: self.key6_pressed, 7: self.key7_pressed,
                        8: None, 9: None,  10: None, 11: None,
                        12: self.key12_pressed, 13: None,  14: self.key14_pressed, 15: self.key15_pressed
                    }

    def activate_iterm(self):
        self._keyboard.send(Keycode.COMMAND, Keycode.CONTROL, Keycode.OPTION, Keycode.I)

    def execute_command(self, command):
        print(f'Executing: {command}')
        time.sleep(0.5)
        self._layout.write(f'{command}\n')

    def key0_pressed(self):
        print('Key 0 press not implemented.')
        
    def key1_pressed(self):
        print('Switching to development board')
        self._keyboard.send(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('meadow mono disable -s /dev/tty.usbmodem3354336F30361')
        
    def key2_pressed(self):
        print('Enable mono one development board in current window')
        self.execute_command('meadow mono enable -s /dev/tty.usbmodem3354336F30361 && meadow listen')
        
    def key3_pressed(self):
        print('Reset the meadow board.')
        self.execute_command('resetmeadow')
        
    def key4_pressed(self):
        print('Key 4 press not implemented.')
        
    def key5_pressed(self):
        print('Key 5 press not implemented.')
        
    def key6_pressed(self):
        print('Writing application to board')
        self.execute_command('meadow file write -f App.dll -t App.exe && meadow file write -f App.pdb')
        
    def key7_pressed(self):
        print('Building software')
        self.execute_command('msbuild ../../..')
        
    def key8_pressed(self):
        print('Key 8 press not implemented.')
        
    def key9_pressed(self):
        print('Key 9 press not implemented.')
        
    def key10_pressed(self):
        print('Key 10 press not implemented.')
        
    def key11_pressed(self):
        print('Key 11 press not implemented.')
        
    def key12_pressed(self):
        print('Starting debug session.')
        self._keyboard.send(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('../debug.sh --server')
        time.sleep(0.2)
        self._keyboard.send(Keycode.COMMAND, Keycode.TWO)
        self.execute_command('../debug.sh')
        
    def key13_pressed(self):
        print('Key 13 press not implemented.')
        
    def key14_pressed(self):
        print('Flashing OS and RT')
        self._keyboard.send(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('disable && monoflash && ../flash.sh && resetmeadow')
        
    def key15_pressed(self):
        print('Building and flashing operating system')
        self._keyboard.send(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('../build.sh && ../flash.sh && resetmeadow')
        
    def key_pressed(self, number):
        if number in self.keys and self.keys[number] is not None:
            self.keys[number]()
        else:
            print(f'Unknown key {number}')