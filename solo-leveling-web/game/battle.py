# game/battle.py (modified healing part)
import random
from game.monster import get_random_monster

def start_battle(player):
    """Starts a battle sequence between player and random monster."""
    monster = get_random_monster()
    print(f"\n⚔️ A wild {monster.name} appears! ⚔️")

    while monster.hp > 0 and player.hp > 0:
        print(f"\nYour HP: {player.hp}/{player.max_hp} | {monster.name} HP: {monster.hp}")
        action = input("1. Attack  2. Heal  3. Run\n> ")

        if action == "1":
            # === PLAYER ATTACKS ===
            damage = player.attack - random.randint(0, monster.attack // 2)
            monster.hp -= max(damage, 0)
            print(f"You hit {monster.name} for {damage} damage!")

        elif action == "2":
            # === PLAYER HEALS ===
            heal_amount = 20
            player.hp = min(player.max_hp, player.hp + heal_amount)
            print(f"You healed {heal_amount} HP! (Now {player.hp}/{player.max_hp})")

            # Monster attacks even when you heal (reduced damage)
            m_damage = max(0, (monster.attack // 2) - (player.defense // 2))
            player.hp -= m_damage
            print(f"{monster.name} attacks while you’re healing! You take {m_damage} damage.")

        elif action == "3":
            print("You ran away!")
            return

        else:
            print("Invalid choice!")

        # === MONSTER'S TURN (if still alive) ===
        if monster.hp > 0 and action != "2":  # already attacked after heal
            m_damage = max(0, monster.attack - (player.defense // 2))
            player.hp -= m_damage
            print(f"{monster.name} hits you for {m_damage} damage!")

    # === BATTLE END ===
    if player.hp <= 0:
        print("\n💀 You were defeated... Game Over.")
        exit()
    else:
        print(f"\n✅ You defeated {monster.name}!")
        player.xp += monster.xp
        player.gold += monster.gold
        if player.xp >= 100:
            player.level_up()
