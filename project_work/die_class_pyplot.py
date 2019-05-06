from random import randint


class Die:
    """Create a die class"""
    def __init__(self, num_sides=6):
        """Assume a six_sided die."""
        self.num_sides = num_sides

        self.x_values = []
        self.y_values = []

    def roll(self):
        """
        Return a random value between 1 and number of sides.
        """
        return randint(1, self.num_sides)