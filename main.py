from Authentication.Signup import signup_user
from Authentication.Signin import signin_user
from Authentication.Exit import exit_program

def main():
    while True:
        print("\n===============================")
        print("  RESTAURANT AUTH SYSTEM")
        print("===============================")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        print("-------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            signup_user()
        elif choice == "2":
            signin_user()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
