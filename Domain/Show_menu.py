import json
import os

MENU_FILE = os.path.join("Database", "menudetails.json")

def view_menu():
    if not os.path.exists(MENU_FILE):
        print(" Menu file not found.")
        input("Press Enter to continue...")
        return

    try:
        with open(MENU_FILE, "r") as f:
            data = json.load(f)
    except Exception:
        print(" Error reading menu file.")
        input("Press Enter to continue...")
        return

    print("\n========================== MENU =============================")
    for category, items in data.items():
        print(f"\n-- {category.upper()} --")
        for i in items:
            # display both half and full prices if they exist
            half = i.get("half_plate", i.get("half_price", "N/A"))
            full = i.get("full_plate", i.get("full_price", "N/A"))
            print(f"ID: {i.get('id')} | {i.get('item')} ({i.get('type')}) | Half: ₹{half} | Full: ₹{full}")
    input("\nPress Enter to continue...")
