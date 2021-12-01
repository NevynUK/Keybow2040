import time

from adafruit_hid.keycode import Keycode

from Keypads import KeypadBase

class WildernessLabsKeypad(KeypadBase.KeypadBase):
    def __init__(self, colour, name, keyboard, layout, consumer_control):
        KeypadBase.KeypadBase.__init__(self, colour, name, keyboard, layout, consumer_control)
        self._keys = {
                        0: None, 1: self.key1_pressed,  2: self.key2_pressed, 3: self.key3_pressed,
                        4: None, 5: None,  6: self.key6_pressed, 7: self.key7_pressed,
                        8: None, 9: None,  10: None, 11: None,
                        12: self.key12_pressed, 13: None,  14: self.key14_pressed, 15: self.key15_pressed
                    }

    def activate_iterm(self):
        self._keyboard.send(Keycode.COMMAND, Keycode.CONTROL, Keycode.OPTION, Keycode.I)

    def key1_pressed(self):
        print('Switching to development board')
        self.send_keystrokes(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('meadow mono disable -s /dev/tty.usbmodem3354336F30361')
        
    def key2_pressed(self):
        print('Enable mono one development board in current window')
        self.execute_command('meadow mono enable -s /dev/tty.usbmodem3354336F30361 && meadow listen')
        
    def key3_pressed(self):
        print('Reset the meadow board.')
        self.execute_command('resetmeadow')
        
    def key6_pressed(self):
        print('Writing application to board')
        self.execute_command('meadow file write -f App.dll -t App.exe && meadow file write -f App.pdb')
        
    def key7_pressed(self):
        print('Building software')
        self.execute_command('msbuild ../../..')
        
    def key12_pressed(self):
        print('Starting debug session.')
        self.send_keystrokes(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('../debug.sh --server')
        time.sleep(0.2)
        self.send_keystrokes(Keycode.COMMAND, Keycode.TWO)
        self.execute_command('../debug.sh')
        
    def key13_pressed(self):
        print('Key 13 press not implemented.')
        
    def key14_pressed(self):
        print('Flashing OS and RT')
        self.send_keystrokes(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('disable && monoflash && ../flash.sh && resetmeadow')
        
    def key15_pressed(self):
        print('Building and flashing operating system')
        self.send_keystrokes(Keycode.COMMAND, Keycode.ONE)
        self.execute_command('../build.sh && ../flash.sh && resetmeadow')

