from datetime import datetime
from art import tprint

def get_employees():
    now = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    tprint(f"[{now}] get_employees", 'handwriting1')

if __name__ == '__main__':
    get_employees()