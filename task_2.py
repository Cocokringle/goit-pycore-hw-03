import random


def get_numbers_ticket(min: int, max:int, quantity: int) -> list[int]:
    try:
        min_val = int(min)
        max_val = int(max)
        quantity_val = int(quantity)
    except ValueError:
        return []
    
    isValid = min_val >= 1 and max_val <= 1000 and min_val <= max_val and 1 <= quantity_val <= (max_val - min_val + 1)

    if(isValid):
        all_numbers = range(min_val, max_val)
        unique_random_numbers = random.sample(all_numbers, quantity_val)
        return sorted(unique_random_numbers)
    else:
        return []


print(get_numbers_ticket(1,1000,9))