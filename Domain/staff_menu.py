import os
from Domain.Show_menu import view_menu
from Domain.order_processing import process_order
from Domain.table_booking import book_table
from Domain.generate_bill import generate_bill

def staff_menu(choice):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("================== STAFF MENU================")
        print("1. View Menu")
        print("2. Process Order")
        print("3. Book Table")
        print("4. Generate Bill")
        print("5. Logout")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            view_menu()
        elif choice == '2':
            process_order()
        elif choice == '3':
            book_table()
        elif choice == '4':
            oid = input("Enter order id to generate bill: ").strip()
            generate_bill(oid)
        elif choice == '5':
            print(" Logging out...")
            input("Press Enter to continue...")
            break
        else:
            print(" Invalid choice.")
            input("Press Enter to continue...")
