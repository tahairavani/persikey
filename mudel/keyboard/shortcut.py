from pynput import keyboard
from collections import defaultdict

class ShortcutManager:
    """this class is for working on shortcuts with pynput.keyboard library.
    for use this :
    add new shortcut to shortcut manager with add_shortcut()
    and start listening with listen function"""
    def __init__(self):
        self.pressed_keys = set()
        self.shortcuts = defaultdict(list)
        
    def add_shortcut(self, keys, callback):
        """add a new shortcut to shortcut manager class
        for use thsi : 
        add_shortcut([add your key from keyboard.Key], callback function)    """
        key_set = set(keys)
        self.shortcuts[frozenset(key_set)].append(callback)
    
    def on_press(self, key):
        """activate this function in press key"""
        self.pressed_keys.add(key)
        self.check_shortcuts()
    
    def on_release(self, key):
        """activate this function in release key"""
        try:
            self.pressed_keys.remove(key)
        except KeyError:
            pass
        
    def check_shortcuts(self):
        """check shortcuts use this on listen function"""
        current_frozen = frozenset(self.pressed_keys)
        if current_frozen in self.shortcuts:
            for callback in self.shortcuts[current_frozen]:
                callback()
    
    def listen (self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            listener.join()

