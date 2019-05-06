class Car():
    """Simulate method for summary."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year

    def update_odometer(self, mileage):
        """Set odometer reading to a given value."""
        self.odometer_reading = mileage

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = "\n" + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement thart show the car's mileage."""
        print("This car has " + str(self.odometer_reading) +
              " miles on it.")



my_old_car = Car('toyota','corolla',2016)

print(my_old_car.get_descriptive_name())

my_old_car.update_odometer(65)
my_old_car.read_odometer()

#Conditions can also be used within classes

class Car():
    """Simulate method for summary."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year

    def update_odometer(self, mileage):
        """Set odometer reading to a given value.
        Reject reduction alterations to the reading."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("You can't roll back the odometer!")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = "\n" + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement thart show the car's mileage."""
        print("This car has " + str(self.odometer_reading) +
              " miles on it.")

my_old_car.update_odometer(45)
my_old_car.read_odometer()


#incrementing a value through a method.

class Car():
    """Simulate method for summary."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year

    def update_odometer(self, mileage):
        """Set odometer reading to a given value."""
        self.odometer_reading = mileage

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = "\n" + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement thart show the car's mileage."""
        print("This car has " + str(self.odometer_reading) +
              " miles on it.")

    def increment_odometer(self,miles):
        """Add the given amount to the odometer."""
        self.odometer_reading += miles


my_used_car = Car('subaru','outback',2013)
print (my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()