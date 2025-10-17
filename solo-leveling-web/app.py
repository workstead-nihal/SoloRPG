from flask import Flask, render_template, request, session
from game.player import Player
from game.monster import Monster
import random

app = Flask(__name__)
app.secret_key = "secret_key_here"  # required for session

# Initialize player and monster
player = Player("Shadow Hunter")
current_monster = Monster("Goblin", 50, 8, 40, 20)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    global current_monster

    if request.method == "POST":
        action = request.form.get("action")

        if action == "attack":
            damage = player.attack - random.randint(0, current_monster.attack // 2)
            current_monster.hp -= max(damage, 0)
            message += f"You hit {current_monster.name} for {damage} damage!<br>"

        elif action == "heal":
            heal_amount = 50
            player.hp = min(player.max_hp, player.hp + heal_amount)
            message += f"You healed {heal_amount} HP! (HP: {player.hp}/{player.max_hp})<br>"

        # Monster attacks after every player action
        if current_monster.hp > 0:
            m_damage = max(0, current_monster.attack - player.defense // 2)
            player.hp -= m_damage
            message += f"{current_monster.name} attacks you for {m_damage} damage!<br>"

        # Monster defeated
        if current_monster.hp <= 0:
            message += f"You defeated {current_monster.name}! You gain {current_monster.xp} XP and {current_monster.gold} gold.<br>"
            player.xp += current_monster.xp
            player.gold += current_monster.gold
            if player.xp >= 100:
                player.level_up()
            # spawn a new monster
            current_monster = Monster("Goblin", 50, 8, 40, 20)

        # Player defeated
        if player.hp <= 0:
            message += "💀 You were defeated... Game Over."
            return render_template("gameover.html")

    return render_template("index.html", player=player, monster=current_monster, message=message)

