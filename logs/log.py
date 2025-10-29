import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.txt")
os.makedirs(LOG_DIR, exist_ok=True)

def log_error(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + "="*50 + "\n")
        f.write(f" Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f" Error: {message}\n")
        f.write("="*50 + "\n")

def log_action(action: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ACTION: {action}\n")
