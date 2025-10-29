import os
from Domain.Show_menu import view_menu
from Domain.menu_crud import add_item, update_item, delete_item
from Domain.order_processing import process_order
from Domain.table_booking import book_table
from Domain.generate_bill import generate_bill
from Report.Report__Sell import ReportSell

def admin_menu(username):
    """Admin main dashboard for D'Magic Taste"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===========================================")
        print(f"ADMIN MENU - D'Magic Taste ({username})")
        print("===========================================")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Update Menu Item")
        print("4. Delete Menu Item")
        print("5. Process Order")
        print("6. Book Table")
        print("7. Generate Bill")
        print("8. Sales Report")
        print("9. Logout")
        print("===========================================")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_menu()

        elif choice == '2':
            add_item()

        elif choice == '3':
            update_item()

        elif choice == '4':
            delete_item()

        elif choice == '5':
            process_order()

        elif choice == '6':
            book_table()

        elif choice == '7':
            oid = input("Enter Order ID to generate bill: ").strip()
            generate_bill(oid)

        elif choice == '8':
            rs = ReportSell()
            rs.generate_report()

        elif choice == '9':
            print(" Logging out...")
            input("Press Enter to continue...")
            break

        else:
            print(" Invalid choice. Please try again.")
            input("Press Enter to continue...")
