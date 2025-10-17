# game/player.py
# --------------------------------------------
# Defines the Player class and its attributes
# --------------------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = 100       # ✅ NEW: maximum HP limit
        self.hp = self.max_hp   # start full health
        self.attack = 10
        self.defense = 5
        self.xp = 0
        self.gold = 0
        self.inventory = {"Potion": 2}  # start with 2 healing potions

    def show_stats(self):
        """Displays player stats in a clean format."""
        print(f"\n=== {self.name}'s Stats ===")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"XP: {self.xp}")
        print(f"Gold: {self.gold}")
        print("===========================")

    def level_up(self):
        """Increases player level and stats when XP >= 100."""
        self.level += 1
        self.max_hp += 20       # ✅ Increase cap, not just current HP
        self.hp = self.max_hp   # heal to full when leveling up
        self.attack += 5
        self.defense += 3
        self.xp = 0
        print(f"\n🔥 {self.name} leveled up! Now Level {self.level}!")

    def show_inventory(self):
        """Displays all items and quantities."""
        print("\n=== Inventory ===")
        for item, qty in self.inventory.items():
            print(f"{item}: {qty}")
        print("=================")
    
    def use_item(self, item_name):
        """Uses an item if available."""
        if item_name in self.inventory and self.inventory[item_name] > 0:
            if item_name == "Potion":
                heal_amount = 50
                self.hp = min(self.max_hp, self.hp + heal_amount)
                print(f"\n💊 You used a Potion and healed {heal_amount} HP! ({self.hp}/{self.max_hp})")
                self.inventory[item_name] -= 1
        else:
            print("\n❌ You don’t have that item!")