from datetime import datetime
from art import tprint
def calculate_salary():
    now = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    tprint(f"[{now}] calculate_salary", 'handwriting1')

if __name__ == '__main__':
    calculate_salary()