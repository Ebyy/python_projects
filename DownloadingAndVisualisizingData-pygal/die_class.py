from random import randint

class Die:
    """Define attributes of this class."""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Simulate rolling the die."""
        return randint(1, self.num_sides)