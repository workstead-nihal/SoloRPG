# game/system.py
# --------------------------------------------
# Utility functions used across the game
# --------------------------------------------
import os, sys, time

def clear_screen():
    """Clears the console screen (works on Windows/Linux/Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    """Prints text slowly to create dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()