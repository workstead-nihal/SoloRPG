# game/monster.py
# --------------------------------------------
# Defines the Monster class and list of monsters
# --------------------------------------------
import random

class Monster:
    def __init__(self, name, hp, attack, xp, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.xp = xp
        self.gold = gold

def get_random_monster():
    """Returns a randomly chosen monster."""
    monster_list = [
        Monster("Goblin", 50, 8, 40, 20),
        Monster("Orc", 80, 12, 60, 35),
        Monster("Shadow Beast", 120, 18, 100, 50)
    ]
    return random.choice(monster_list)
