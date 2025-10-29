import json
import os
import uuid
from datetime import datetime

MENU_FILE = os.path.join("Database", "menudetails.json")
ORDER_FILE = os.path.join("Database", "orderdetails.json")

def process_order():
    os.makedirs("Database", exist_ok=True)
    if not os.path.exists(MENU_FILE):
        print(" Menu file not found. Please ask admin to add menu.")
        input("Press Enter to continue...")
        return

    with open(MENU_FILE, "r") as f:
        menu = json.load(f)

    # simple flow: choose category -> choose item id -> qty -> add
    items_for_order = []
    while True:
        print("\nAvailable categories:")
        for c in menu.keys():
            print(" -", c)
        cat = input("Choose category (or 'q' to finish): ").strip()
        if cat.lower() == 'q':
            break
        if cat not in menu:
            print(" Invalid category.")
            continue
        for it in menu[cat]:
            print(f"ID:{it['id']} | {it['item']} | Half: ₹{it['half_plate']} | Full: ₹{it['full_plate']}")
        try:
            iid = int(input("Enter item ID: ").strip())
        except ValueError:
            print(" ID must be integer.")
            continue
        item = next((x for x in menu[cat] if x.get("id") == iid), None)
        if not item:
            print(" Item ID not found.")
            continue
        try:
            qty = int(input("Quantity: ").strip())
        except ValueError:
            print(" Quantity must be integer.")
            continue
        # store price placeholders; final choice half/full done at bill time
        items_for_order.append({
            "item": item['item'],
            "id": item['id'],
            "type": item['type'],
            "qty": qty,
            "price_half": item.get("half_plate"),
            "price_full": item.get("full_plate")
        })
        print(" Item added to order.")
        cont = input("Add more items? (Y/N): ").strip().lower()
        if cont != 'y':
            break

    if not items_for_order:
        print(" No items in order.")
        input("Press Enter to continue...")
        return

    order_id = "ORD-" + uuid.uuid4().hex[:6].upper()
    order_obj = {
        "order_id": order_id,
        "items": items_for_order,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "total_amount": 0  
    }

    orders = []
    if os.path.exists(ORDER_FILE):
        try:
            with open(ORDER_FILE, "r") as f:
                orders = json.load(f)
        except Exception:
            orders = []

    orders.append(order_obj)
    with open(ORDER_FILE, "w") as f:
        json.dump(orders, f, indent=4)

    print(f"\n Order placed successfully! Order ID: {order_id}")
    input("Press Enter to continue...")
