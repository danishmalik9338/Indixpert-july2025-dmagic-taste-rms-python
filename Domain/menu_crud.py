import json
import os

MENU_FILE = os.path.join("Database", "menudetails.json")

def _load_menu():
    os.makedirs("Database", exist_ok=True)
    if not os.path.exists(MENU_FILE):
        with open(MENU_FILE, "w") as f:
            json.dump({}, f)
    try:
        with open(MENU_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def _save_menu(data):
    with open(MENU_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_item():
    data = _load_menu()
    category = input("Enter category (e.g., dinner, beverages): ").strip()
    try:
        new_id = int(input("Enter new item id (int): ").strip())
    except ValueError:
        print(" ID must be integer.")
        input("Press Enter to continue...")
        return
    name = input("Item name: ").strip()
    typ = input("Type (Veg/Non-Veg): ").strip()
    try:
        half = float(input("Half plate price: ").strip())
        full = float(input("Full plate price: ").strip())
    except ValueError:
        print(" Price must be number.")
        input("Press Enter to continue...")
        return

    item = {"id": new_id, "item": name, "type": typ, "half_plate": half, "full_plate": full}
    data.setdefault(category, []).append(item)
    _save_menu(data)
    print(" Item added.")
    input("Press Enter to continue...")

def update_item():
    data = _load_menu()
    cat = input("Enter category of item: ").strip()
    try:
        item_id = int(input("Enter item id to update: ").strip())
    except ValueError:
        print(" ID must be integer.")
        input("Press Enter to continue...")
        return
    items = data.get(cat, [])
    item = next((i for i in items if i.get("id") == item_id), None)
    if not item:
        print(" Item not found.")
        input("Press Enter to continue...")
        return
    print(f"Updating {item['item']}")
    name = input(f"Name [{item['item']}]: ").strip() or item['item']
    typ = input(f"Type [{item['type']}]: ").strip() or item['type']
    try:
        half_input = input(f"Half [{item.get('half_plate')}]: ").strip()
        full_input = input(f"Full [{item.get('full_plate')}]: ").strip()
        half = float(half_input) if half_input else item.get('half_plate')
        full = float(full_input) if full_input else item.get('full_plate')
    except ValueError:
        print(" Price must be number.")
        input("Press Enter to continue...")
        return
    item.update({"item": name, "type": typ, "half_plate": half, "full_plate": full})
    _save_menu(data)
    print(" Item updated.")
    input("Press Enter to continue...")

def delete_item():
    data = _load_menu()
    cat = input("Enter category of item: ").strip()
    try:
        item_id = int(input("Enter item id to delete: ").strip())
    except ValueError:
        print(" ID must be integer.")
        input("Press Enter to continue...")
        return
    items = data.get(cat, [])
    new_items = [i for i in items if i.get("id") != item_id]
    if len(new_items) == len(items):
        print(" Item not found.")
    else:
        data[cat] = new_items
        _save_menu(data)
        print(" Item deleted.")
    input("Press Enter to continue...")
