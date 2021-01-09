import random


def generate_user_id():
    total = ''
    for i in range(10):
        total += str(random.randint(0, 9))
        if i % 2 == 0:
            total += '-'

    return total
