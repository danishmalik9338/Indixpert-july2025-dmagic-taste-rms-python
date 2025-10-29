import sys
from logs.log import log_action

def exit_program():
    print("\n Thank you for visiting D'Magic Taste!")
    log_action("Application exited by user.")
    sys.exit()
