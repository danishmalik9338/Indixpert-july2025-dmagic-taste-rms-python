import json
import os
import getpass
from Validation.valid_email import validate_email
from Validation.valid_password import validate_password
from Validation.valid_name import validate_name
from logs.log import log_action

USERS_FILE = os.path.join("Database", "customerdetails.json")

def signup_user():
    os.makedirs("Database", exist_ok=True)
    print("\n=== SIGN UP ===")
    name = input("Enter your name: ").strip()
    if not validate_name(name):
        print(" Invalid name. Only alphabets and spaces allowed.")
        input("Press Enter to continue...")
        return

    email = input("Enter your email: ").strip()
    if not validate_email(email):
        print(" Invalid email format.")
        input("Press Enter to continue...")
        return

    password = getpass.getpass("Enter password: ")
    if not validate_password(password):
        print(" Password must be at least 8 chars, include upper, lower, digit, special.")
        input("Press Enter to continue...")
        return

    role = input("Enter role (admin/staff): ").strip().lower()
    if role not in ["admin", "staff"]:
        print(" Invalid role. Choose either 'admin' or 'staff'.")
        input("Press Enter to continue...")
        return

    data = []
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r") as f:
                data = json.load(f)
        except Exception:
            data = []

    if any(u.get("email") == email for u in data):
        print(" User already exists.")
        input("Press Enter to continue...")
        return

    new_user = {"name": name, "email": email, "password": password, "role": role}
    data.append(new_user)
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)

    log_action(f"New user signed up: {email} ({role})")
    print(" Signup successful!")
    input("Press Enter to continue...")
