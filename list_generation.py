import random

def generate_starting_list(n, min_val, max_val):
    lst = []
    for i in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

