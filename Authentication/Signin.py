import json
import os
import getpass
from Domain.admin_menu import admin_menu
from Domain.staff_menu import staff_menu
from logs.log import log_action

USERS_FILE = os.path.join("Database", "customerdetails.json")

def signin_user():
    os.makedirs("Database", exist_ok=True)
    if not os.path.exists(USERS_FILE):
        print(" No users found. Please sign up first.")
        input("Press Enter to continue...")
        return

    email = input("Enter email: ").strip()
    password = getpass.getpass("Enter password: ")

    try:
        with open(USERS_FILE, "r") as f:
            users = json.load(f)
    except Exception:
        users = []

    for u in users:
        if u.get("email") == email and u.get("password") == password:
            print(f"\n Login successful! Welcome {u.get('name').title()} ({u.get('role').upper()})")
            log_action(f"User logged in: {email}")
            input("Press Enter to continue...")
            if u.get("role") == "admin":
                admin_menu(u.get("name"))
            else:
                staff_menu(u.get("name"))
            return

    print(" Invalid credentials.")
    input("Press Enter to continue...")
