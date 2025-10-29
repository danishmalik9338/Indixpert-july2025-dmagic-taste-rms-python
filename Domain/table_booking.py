import json
import os
from datetime  import datetime
from Validation.valid_date import validate_date
from Validation.valid_time import validate_time
from Validation.valid_table import validate_table

TABLE_FILE = os.path.join("Database", "tabledetails.json")

def _ensure_tables():
    # create default 10 tables if file not exist
    if not os.path.exists(TABLE_FILE):
        tables = [{"table_id": i, "seats": 4, "status": "available"} for i in range(1, 21)]
        with open(TABLE_FILE, "w") as f:
            json.dump(tables, f, indent=4)

def book_table():
    os.makedirs("Database", exist_ok=True)
    _ensure_tables()
    with open(TABLE_FILE, "r") as f:
        tables = json.load(f)

    print("\nCurrent tables:")
    for t in tables:
        print(f"Table {t['table_id']} | Seats: {t['seats']} | Status: {t['status']}")

    table_id = input("Enter table id to book: ").strip()
    if not validate_table(table_id, total_tables=len(tables)):
        print(" Invalid table id.")
        input("Press Enter to continue...")
        return

    date = input("Enter booking date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        print(" Invalid date format.")
        input("Press Enter to continue...")
        return

    time = input("Enter time (HH:MM 24hr): ").strip()
    if not validate_time(time):
        print(" Invalid time format.")
        input("Press Enter to continue...")
        return

    # find table
    tid = int(table_id)
    table = next((x for x in tables if x.get("table_id") == tid), None)
    if not table:
        print(" Table not found.")
        input("Press Enter to continue...")
        return

    if table.get("status") != "available":
        print(" Table is not available.")
        input("Press Enter to continue...")
        return

    # mark booked
    table['status'] = 'booked'
    table['booking_date'] = date
    table['booking_time'] = time

    with open(TABLE_FILE, "w") as f:
        json.dump(tables, f, indent=4)

    print(f" Table {tid} booked for {date} at {time}.")
    input("Press Enter to continue...")
