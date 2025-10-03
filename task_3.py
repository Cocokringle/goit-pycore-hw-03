import re 

def normalize_phone(phone_number: str) -> str:
    try:
        clean_number = re.sub(r'[^\d\+]', '', phone_number)
        if len(clean_number) == 0:
            return ''
        elif clean_number.startswith('+') and len(clean_number) == 13:
            return clean_number
        elif clean_number.startswith('380') and len(clean_number) == 12:
            return f"+{clean_number}"
        elif len(clean_number) == 10:
            return f"+38{clean_number}"
        else:
            return f"+380{clean_number}"
        
    except (ValueError, TypeError):
        print('Invalid data format')
        return ''


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Sanitized numbers for sms:", sanitized_numbers)