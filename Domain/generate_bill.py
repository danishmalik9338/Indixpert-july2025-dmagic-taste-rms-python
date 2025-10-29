import json
import os
import uuid
from datetime import datetime

ORDER_FILE = os.path.join("Database", "orderdetails.json")
BILL_FILE = os.path.join("Database", "bill_records.json")

def continue_prompt(message="Do you want to continue? (Y/N): "):
    choice = input(message).strip().lower()
    return choice == 'y'

def generate_bill(order_id):
    os.makedirs("Database", exist_ok=True)

    if not os.path.exists(ORDER_FILE):
        print(" Order file not found.")
        if not continue_prompt(): return
        return

    try:
        with open(ORDER_FILE, "r") as f:
            orders = json.load(f)
    except Exception:
        print(" Error reading order file.")
        if not continue_prompt(): return
        return

    order = next((o for o in orders if o.get("order_id") == order_id), None)
    if not order:
        print(" Order not found.")
        if not continue_prompt(): return
        return

    print("\n ORDER DETAILS")
    print("=" * 60)
    total_amount = 0
    updated_items = []

    for item in order.get("items", []):
        print(f"\nItem: {item.get('item')} | Type: {item.get('type')} | Qty: {item.get('qty')}")
        # ask half/full with validation
        while True:
            hf = input("Half or Full? (H/F): ").strip().lower()
            if hf in ['h', 'f']:
                break
            print(" Enter H or F.")
        price = item.get("price_half") if hf == 'h' else item.get("price_full")
        line_total = price * item.get("qty", 1)
        total_amount += line_total
        updated_items.append({
            "item": item.get("item"),
            "qty": item.get("qty"),
            "type": item.get("type"),
            "portion": "Half" if hf == 'h' else "Full",
            "price": price,
            "line_total": line_total
        })

    print("\n========================================")
    print(" ****************BILL SUMMARY*************")
    print("==========================================")
    for it in updated_items:
        print(f"{it['item']} ({it['portion']}) x {it['qty']} = ₹{it['line_total']}")
    print("========================================")
    print(f" TOTAL AMOUNT: ₹{total_amount}")

    # Payment modes with validation
    print("\n ========PAYMENT METHOD========")
    print("1. Cash\n2. UPI\n3. Credit Card\n4. Debit Card")
    while True:
        pay_choice = input("Select Payment Mode (1-4): ").strip()
        if pay_choice in ["1", "2", "3", "4"]:
            break
        print(" Invalid choice. Try again.")

    payment_modes = {"1": "Cash", "2": "UPI", "3": "Credit Card", "4": "Debit Card"}
    payment_method = payment_modes[pay_choice]

    if not continue_prompt("Do you want to confirm and save this bill? (Y/N): "):
        print("↩  Bill generation cancelled.")
        return

    bill_id = "BILL-" + uuid.uuid4().hex[:6].upper()
    date_now = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")

    new_bill = {
        "bill_id": bill_id,
        "order_id": order_id,
        "items": updated_items,
        "total_amount": total_amount,
        "payment_mode": payment_method,
        "date": date_now,
        "time": time_now
    }

    bills = []
    if os.path.exists(BILL_FILE):
        try:
            with open(BILL_FILE, "r") as f:
                bills = json.load(f)
        except Exception:
            bills = []

    bills.append(new_bill)
    with open(BILL_FILE, "w") as f:
        json.dump(bills, f, indent=4)

    # update order's total_amount (optional)
    try:
        for o in orders:
            if o.get("order_id") == order_id:
                o["total_amount"] = total_amount
        with open(ORDER_FILE, "w") as f:
            json.dump(orders, f, indent=4)
    except Exception:
        pass

    print("\n Bill generated successfully!")
    print(f" Bill ID: {bill_id}")
    print(f" Payment Mode: {payment_method}")
    input("\nPress Enter to continue...")
