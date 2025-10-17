# game/story.py
# --------------------------------------------
# Handles the game's story and intro text
# --------------------------------------------
from game.system import slow_print

def intro_story(player):
    """Intro cutscene when the game starts."""
    slow_print(f"\n[System]: Welcome, {player.name}.")
    slow_print("You are an E-Rank Hunter... barely surviving low-level dungeons.")
    slow_print("But fate has chosen you.")
    slow_print("After today... everything will change.")
    slow_print("[System]: You have awakened the ability to LEVEL UP.")
