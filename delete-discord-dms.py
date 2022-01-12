from pynput.keyboard import Key, Controller
from pynput import mouse
import time

keyboard = Controller()
mouseController = mouse.Controller()

confirmed = input('Discord Message Deleter  Copyright (C) 2021  D Brinson\n\
    This program comes with ABSOLUTELY NO WARRANTY.\n\
    Actually, DON\'T use this program!\n\
    This is free software, and you are welcome to redistribute it\n\
    under the conditions of the GNU GPL version 3.\n\
    If you still want to operate this program at your own risk,\n\
    type Y and open the conversation you want to clean within 5 seconds.\n\
    \n\n\
    Would you like to continue? [y/N] ')

if confirmed.lower() != 'y':
    exit('User wisely requested abort.')

for i in range(5,0,-1):
    print(i)
    time.sleep(1)

print('starting...')

while(True):
    mouseController.press(mouse.Button.left)
    time.sleep(0.1)
    keyboard.press(Key.up)
    time.sleep(0.2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(0.2)
    keyboard.press(Key.backspace)
    time.sleep(0.2)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.press(Key.enter)
    time.sleep(0.4)
