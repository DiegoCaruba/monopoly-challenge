import logging
from random import choice, randint


def flip_a_coin():
    return choice([True, False])


def throw_dice() -> int:
    return randint(1, 6)


logging.basicConfig(level=logging.INFO)
def logger(msg: str):
    logging.info(msg)
