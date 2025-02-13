import random


def flip_a_coin():
    return random.choice([True, False])


def throw_dice() -> int:
    return random.randint(1, 6)
