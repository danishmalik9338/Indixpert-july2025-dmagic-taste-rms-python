from datetime import datetime

def validate_date(date_str: str) -> bool:
    for fmt in ("%Y-%m-%d", "%d-%m-%Y"):
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False
