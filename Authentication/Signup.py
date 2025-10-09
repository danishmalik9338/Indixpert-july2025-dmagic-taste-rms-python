import json
import os
import getpass
import re

USER_Path = os.path.join("Databass", "customerdetails.json")

def load_users():
    if not os.path.exists(USER_Path):
        os.makedirs(os.path.dirname(USER_Path), exist_ok=True)
        with open(USER_Path, "w") as f:
            json.dump([], f)
    with open(USER_Path, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_Path, "w") as f:
        json.dump(users, f, indent=4)

def signup_user():
    print("\n===== USER SIGNUP =====")
    users = load_users()
    username = input("Enter username: ").strip()

    for user in users:
        if user["username"].lower() == username.lower():
            print("Username already exists! Please choose another.")
            return

    while True:
        password = getpass.getpass("Enter password (8 characters): ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password != confirm_password:
            print("Passwords do not match! Try again.")
            continue
        if len(password) != 8:
            print("Password must be exactly 8 characters long.")
            continue
        if password == "00000000":
            print("⚠️ Password cannot be '00000000'. Choose a stronger password.")
            continue
        break

    email = input("Enter email: ").strip()

    while True:
        phone = input("Enter phone number: ").strip()
        if not re.match(r'^\d{10}$', phone):
            print("⚠️ Phone number must be exactly 10 digits (e.g., 9876543210).")
            continue
        if phone == "0000000000":
            print("⚠️ Phone number cannot be '0000000000'. Enter a valid number.")
            continue
        break

    new_user = {
        "username": username,
        "password": password,
        "email": email,
        "phone": phone
    }

    users.append(new_user)
    save_users(users)
    print(f"Signup successful! Welcome, {username}!")
