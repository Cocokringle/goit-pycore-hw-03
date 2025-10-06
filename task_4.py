

from datetime import datetime, timedelta


users = [
    {"name": "John Doe", "birthday": "1985.10.06"},
    {"name": "Jane Smith", "birthday": "1990.10.11"}
]

def get_upcoming_birthdays(users):
    try:
        today = datetime.today().date()
        upcoming_birthdays = []

        for user in users:
            birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = birthday_date.replace(today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_date.replace(today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year
                birthday_on_saturday = congratulation_date.weekday() == 5 
                birthday_on_monday =  congratulation_date.weekday() == 6

                if birthday_on_saturday:
                    congratulation_date += timedelta(2)
                elif birthday_on_monday:
                    congratulation_date += timedelta(1)

                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })

                return upcoming_birthdays
    
    except (TypeError,ValueError):
        print('Invalid data format')



print(get_upcoming_birthdays(users))