class Employee():
    """List function definition of methods"""

    def __init__(self, first, last, annual_salary):
        """Define attributes."""
        self.first = first.title()
        self.last = last.title()
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Raise annual income by $5000."""
        self.annual_salary += amount
