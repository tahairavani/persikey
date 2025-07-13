from mudel.keyboard import selected_text,shortcut
from mudel import converter
from pynput.keyboard import Key,KeyCode
from mudel.digits import Digits
import time
def test():
    print("shortcut valid")
def run_shortcut():
    print("app detect short cut")
    time.sleep(1)
    user_text = selected_text.get_selected_text()
    print("app give your text")
    time.sleep(1)
    if Digits.detect_language(user_text) == "english":
        converted_text = converter.Convert(user_text,"english").convert_to_persian()
    elif converter.detect_language(user_text) == "persian":
        converted_text = converter.Convert(user_text,"persian").convert_to_english()
    selected_text.set_selected_text(converted_text)       
    print("app convert and set your text")
shortcut_manager = shortcut.ShortcutManager()
shortcut_manager.add_shortcut(
    [Key.ctrl, Key.alt, KeyCode.from_char('v')],
    run_shortcut
)

if __name__ == "__main__":
    print("""start app
    lisening into shortcuts :) ctrl+alt+v""")
    shortcut_manager.listen()