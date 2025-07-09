import keyboard
import pyperclip 
import time

class ShortCuts :
    """ this class work on persikey shortcuts and read and replace user clipboard """
    COPY_SHORTCUT = "ctrl+c"
    PASTE_SHORTCUT = "ctrl+v"

    def __init__(self):
        self.HOT_KEY = "ctrl+alt+v"


        

    @classmethod
    def get_user_selected_string(cls):
        """this function for copy user selected string and read as clipboard"""
        keyboard.send(ShortCuts.COPY_SHORTCUT)
        time.sleep(0.2)
        clipboard_text = pyperclip.paste()
        return clipboard_text
    
    @classmethod
    def return_and_copy_to_clipboard(cls, string):
        """ this function at first copy string to clipboard and last paste to user selected input """
        pyperclip.copy(string)
        time.sleep(0.2)
        keyboard.send(ShortCuts.PASTE_SHORTCUT)
    
    

ShortCuts.return_and_copy_to_clipboard("hello")