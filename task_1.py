from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - datetime_object

        return delta.days
    except (ValueError, TypeError):
        print('Invalid date format')

        
print(get_days_from_today('2025-12-12'))