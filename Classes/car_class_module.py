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
        return long_name.title()

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


#Multiple classes can also be stored in a single module provided they are related.

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=65):
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print ("\nThis car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this
        battery provides."""
        if self.battery_size < 85:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + \
                  str(range)
        message +=  " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Initialise battery capacity upgrade to 85."""
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print ("\n- Your battery has already been upgraded!")

class Electric_Car(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """"Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car."""

        super().__init__(make,model,year)
        self.battery = Battery()