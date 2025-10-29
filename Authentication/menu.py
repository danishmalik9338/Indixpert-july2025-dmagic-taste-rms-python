import os
from Authentication.Signup import signup_user
from Authentication.Signin import signin_user
from Authentication.exit_program import exit_program

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================================")
        print(" *****************Welcome to D'Magic*************** ")
        print("====================================================")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            signup_user()
        elif choice == '2':
            signin_user()
        elif choice == '3':
            exit_program()
        else:
            print(" Invalid choice. Try again.")
            input("Press Enter to continue...")
