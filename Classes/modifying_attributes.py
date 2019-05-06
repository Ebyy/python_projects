class Car():
    """Simulate method for summary."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  #the default attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = "\n" + str(self.year) + ' ' + self.make + ' ' +\
                    self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement thart show the car's mileage."""
        print("This car has " + str(self.odometer_reading) +
              " miles on it.")


#to modify an attribute can be done directly e.g.
my_new_car = Car('audi','a4',2017)

my_new_car.odometer_reading = 42
my_new_car.read_odometer()

#OR by method








