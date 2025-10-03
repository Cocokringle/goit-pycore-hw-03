from datetime import datetime
import re

def is_valid_date(date_str):
    pattern = r'(19\d\d|20\d\d)-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])'
    return bool(re.match(pattern, date_str))

def get_days_from_today(date: str) -> int:
    if is_valid_date(date):
        print('date valid')
        datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - datetime_object

        return delta.days
    else:
        print('Invalid date format')


print(get_days_from_today('2025-12-12'))