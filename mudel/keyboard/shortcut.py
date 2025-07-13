from pynput import keyboard
from collections import defaultdict, deque
import time
from pynput.keyboard import Key, KeyCode

class ShortcutManager:
    def __init__(self, sequence_timeout=1.0):
        self.sequence_timeout = sequence_timeout
        self.current_sequence = []
        self.last_key_time = time.time()
        self.required_sequences = defaultdict(list)
        self.expected_sequences = {}

    def add_shortcut(self, keys, callback):
        """Add a sequence shortcut that requires holding keys in order"""
        normalized = tuple(self._normalize_key(k) for k in keys)
        self.required_sequences[normalized].append(callback)

    def _normalize_key(self, key):
        """Normalize key for consistent comparison"""
        if isinstance(key, KeyCode):
            return key.char.lower() if key.char else key.vk
        return key

    def on_press(self, key):
        current_time = time.time()
        normalized = self._normalize_key(key)

        # Reset if too much time between key presses
        if current_time - self.last_key_time > self.sequence_timeout:
            self.current_sequence.clear()
            self.expected_sequences.clear()

        self.last_key_time = current_time

        # Add to sequence if not already in current sequence
        if not self.current_sequence or self.current_sequence[-1] != normalized:
            self.current_sequence.append(normalized)

        # Check for matching sequences
        self._check_sequences()

    def on_release(self, key):
        normalized = self._normalize_key(key)
        current_sequence = tuple(self.current_sequence)

        # Check if this completes any sequence
        for seq, callbacks in self.required_sequences.items():
            if current_sequence == seq:
                # Verify all keys in sequence have been pressed
                if all(k in current_sequence for k in seq):
                    for callback in callbacks:
                        callback()
                    self.current_sequence.clear()
                    return

        # Remove from current sequence if released
        if normalized in self.current_sequence:
            self.current_sequence.remove(normalized)

    def _check_sequences(self):
        current_sequence = tuple(self.current_sequence)
        
        # Check for partial matches
        for seq in self.required_sequences:
            if current_sequence == seq[:len(current_sequence)]:
                return  # Still matching, wait for more keys

        # If no partial match, reset
        if current_sequence and not any(
            seq[:len(current_sequence)] == current_sequence
            for seq in self.required_sequences
        ):
            self.current_sequence.clear()

    def listen(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            listener.join()