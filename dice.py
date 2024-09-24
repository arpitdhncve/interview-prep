import random


class Dice:

    @staticmethod
    def roll_dice():
        return random.randint(1,6)