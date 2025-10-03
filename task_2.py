import random


def get_numbers_ticket(min: int, max:int, quantity: int) -> list:
    isValid = min >= 1 and max <= 1000 and min <= max and 1 <= quantity <= (max - min + 1)
    if(isValid):
        all_numbers = range(min, max)
        unique_random_numbers = random.sample(all_numbers, quantity)
        return sorted(unique_random_numbers)
    else:
        return []


print(get_numbers_ticket(1,1000,9))