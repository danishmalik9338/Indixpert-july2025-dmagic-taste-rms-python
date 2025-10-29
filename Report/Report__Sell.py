import json
import os
from datetime import datetime

ORDER_FILE = os.path.join("Database", "orderdetails.json")
REPORT_FILE = os.path.join("Database", "report.json")

class ReportSell:
    def generate_report(self):
        os.makedirs("Database", exist_ok=True)
        if not os.path.exists(ORDER_FILE):
            print(" No order file found.")
            input("Press Enter to continue...")
            return

        try:
            with open(ORDER_FILE, "r") as f:
                orders = json.load(f)
        except Exception:
            print(" Error reading order file.")
            input("Press Enter to continue...")
            return

        if not orders:
            print(" No orders found.")
            input("Press Enter to continue...")
            return

        total_sales = sum(o.get("total_amount", 0) for o in orders)
        report_data = {
            "report_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_orders": len(orders),
            "total_sales": total_sales,
            "top_3_orders": sorted(orders, key=lambda x: x.get("total_amount", 0), reverse=True)[:3]
        }

        with open(REPORT_FILE, "w") as f:
            json.dump(report_data, f, indent=4)

        print("\n Sales Report Generated Successfully!")
        print(f" Date: {report_data['report_date']}")
        print(f" Total Orders: {report_data['total_orders']}")
        print(f" Total Sales: ₹{report_data['total_sales']}")
        input("Press Enter to continue...")
