class Car():
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make +\
                    ' ' + self.model
        return long_name

    def read_odometer(self):
        print ("This car has " + str(self.odometer_reading) +
               " miles on it")

    def update_odometer(self,mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odoometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Inform user on when to perform this taask."""
        print("Refill is needed after 10 miles of driving.")


class Electric_Car(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """"Initialise attributes of the parent class."""
        super().__init__(make,model,year)
        """Attributes and methods specific to the child class can also be added."""
        self.battery_size = 70

    def describe_battery(self):
        """Print description statement."""
        print ("This car has a " + str(self.battery_size) +
               "-kWh battery.")

    def fill_gas_tank(self):
        """Attributes can also be overidden from the
        parent class simply by redefining the attribute
        in the child class (like is done with variables)."""
        print("This car doesn't need a gas tank!")


my_tesla = Electric_Car('tesla','model s',2016)
print (my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()