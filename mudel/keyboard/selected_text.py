import pyperclip
from pynput.keyboard import Key , Controller
import time

def get_selected_text():
    """this function press ctrl+c and return into clipboard"""
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    time.sleep(0.52)
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.52)

    return pyperclip.paste() #return into clipboard

def set_selected_text(text):
    pyperclip.copy(text)
    time.sleep(0.52)
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    time.sleep(0.52)
    keyboard.release(Key.ctrl)
    keyboard.release('v')

time.sleep(5)
set_selected_text("in yek matn copy shode asttttt  ) : ")