class Cat():
    """A simple attempt to model a cat."""    #functions inside classes are called methods

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a cat sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print (self.name.title() + " rolling over!")

#An instance is what the examples we give the class to run like my_cat is an instance.
my_cat = Cat('kim',2)

print ("My cat's name is " + my_cat.name.title() + ".")
print ("My cat is " + str(my_cat.age) + " years old.")

my_cat.sit()
my_cat.roll_over()

#multiple instances can be created
my_cat = Cat('kim',2)
your_cat = Cat('andy',5)
their_cat = Cat('ginger',3)

print ("\nYour cat's name is " + your_cat.name.title() + ".")
print ("Your cat is " + str(your_cat.age) + " years old.")
your_cat.sit()

print ("\nMy cat's name is " + my_cat.name.title() + ".")
print ("My cat is " + str(my_cat.age) + " years old.")
my_cat.sit()

print ("\nTheir cat's name is " + their_cat.name.title() + ".")
print ("Their cat is " + str(their_cat.age) + " years old.")
their_cat.roll_over()


class Car():
    """Simulate method for summary."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = "\n" + str(self.year) + ' ' + self.make + ' ' +\
                    self.model
        return long_name.title()

my_new_car = Car('audi','a3',2016)
print (my_new_car.get_descriptive_name())

his_old_car = Car('honda','accord',2006)
print(his_old_car.get_descriptive_name())

#an attribute can also be set as default.

class Car():
    """Simulate method for summary."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0    # the default attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = "\n" + str(self.year) + ' ' + self.make + ' ' +\
                    self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement thart show the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi','a4',2017)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

