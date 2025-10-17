# game/shop.py
def visit_shop(player):
    """Player can buy items from the shop."""
    shop_items = {
        "Potion": 30,    # 30 gold per potion
        "Elixir": 100    # optional stronger healing item later
    }

    print("\n=== Welcome to the Shop ===")
    print(f"Gold: {player.gold}")
    print("Items for sale:")
    for idx, (item, price) in enumerate(shop_items.items(), start=1):
        print(f"{idx}. {item} - {price} Gold")

    print(f"{len(shop_items)+1}. Exit Shop")

    choice = input("> ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(shop_items):
            item_name = list(shop_items.keys())[choice - 1]
            price = shop_items[item_name]
            if player.gold >= price:
                player.gold -= price
                player.inventory[item_name] = player.inventory.get(item_name, 0) + 1
                print(f"\n✅ You bought 1 {item_name}!")
            else:
                print("\n❌ Not enough gold!")
        else:
            print("\nExiting shop...")
    else:
        print("\nInvalid choice!")
