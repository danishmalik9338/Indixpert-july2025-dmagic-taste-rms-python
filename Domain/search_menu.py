import json
import os

MENU_FILE = os.path.join("Database", "menudetails.json")

def search_menu():
    if not os.path.exists(MENU_FILE):
        print(" Menu file not found.")
        input("Press Enter to continue...")
        return

    term = input(" Search item name or ID: ").strip().lower()
    with open(MENU_FILE, "r") as f:
        data = json.load(f)

    found = []
    for category, items in data.items():
        for i in items:
            if term.isdigit() and int(term) == i.get("id"):
                found.append((category, i))
            elif term in i.get("item", "").lower():
                found.append((category, i))

    if not found:
        print(" No matching items.")
    else:
        for cat, it in found:
            print(f"[{cat}] ID: {it['id']} | {it['item']} | Type: {it['type']} | Half: ₹{it.get('half_plate')} | Full: ₹{it.get('full_plate')}")
    input("Press Enter to continue...")
