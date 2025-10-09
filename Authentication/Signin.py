import json
import os
import getpass

USER_Path = os.path.join("Databass", "customerdetails.json")

def load_users():
    if not os.path.exists(USER_Path):
        return []
    with open(USER_Path, "r") as f:
        return json.load(f)

def signin_user():
    print("\n===== USER LOGIN =====")
    users = load_users()

    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ")

    for user in users:
        if user["username"].lower() == username.lower() and user["password"] == password:
            print(f"Login successful! Welcome back, {username}!")
            return True

    print("Invalid username or password!")
    return False
