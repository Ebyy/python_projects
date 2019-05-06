#Ex. 9-6
class Restaurant():
    """Create attribute for the class using methods"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Simulate a few descriptions."""
        print ("\n" + self.restaurant_name.title() +
               " serves wonderful " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Simulate an annoucement"""
        print(self.restaurant_name.title() + " is now open for the evening.")

    def set_number_served(self,number_served):
        """Simulate setting the number served."""
        self.number_served = number_served

    def increament_number_served(self,additional_number):
        """Initialize to allow the number of people served to be increaed."""
        self.number_served += additional_number


class IceCreamStand(Restaurant):
    """Define attributes of the parent class."""
    def __init__(self,restaurant_name,cuisine_type='ice cream'):
        """Initialise attributes of the parent class."""
        super().__init__(restaurant_name,cuisine_type)

    def flavors(self):
        """Define flavours."""
        self.flavors = []

    def show_flavors(self):
        """Print statement listing available flavours."""
        print ("\nWe have the following flavors available: ")
        for flavor in self.flavors:
            print ("- " + flavor.title())



my_ice_cream = IceCreamStand('ben & jerry')
my_ice_cream.flavors =['orange','grapefruit','mango']
my_ice_cream.describe_restaurant()
my_ice_cream.show_flavors()


#Ex.9-7
class Users():
    """Use methods to define."""

    def __init__(self, first_name, last_name,location,age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts =3

    def describe_user(self):
        """Summarize the informaation collected."""
        print ("\nUser is " + self.first_name.title() +
               " " + self.last_name.title() + " who is " +
               str(self.age) + " years old and from " +
               self.location.title() + ".")

    def greet_user(self):
        """Simulate greeting user."""
        print ("\nHello " + self.first_name.title() + "!")
        print ("Thank you for joining our site from " +
               self.location.title() + ".")


    def increment_login_attempts(self,increment):
        """Allow users to inrease logins by 1."""
        self.login_attempts += increment

    def reset_login_attempt(self,reset):
        """Simulate that it returns the value of login attempts to 0."""
        self.login_attempts = reset

        if reset >= 1:
            self.login_attempts = 0

        else:
            print ("\nThe system has already been reset.")

    def read_attempts(self):
        """Summarize login."""
        print ("You have logged in " + str(self.login_attempts) + " times.")

class Admin(Users):
    """Simulate link between child class and parent class."""
    def __init__(self,first_name,last_name,location,age):
        """Initialise attributes of the parent class."""
        super().__init__(first_name,last_name,location,age)
        self.privileges = []

    def show_privileges(self):
        """Print out list of privileges reserved for Admin."""
        print ("\n" + self.first_name + ' ' + self.last_name +
               ", is the administrator and has the following privileges:")
        for privilege in self.privileges:
            print ("- " + privilege)


administrator = Admin('Ken','fowler','toronto',29)
administrator.privileges =['can add post','can delete post','can ban user']

administrator.describe_user()
administrator.show_privileges()


#Ex 9-8
class User():
    """Use methods to define."""

    def __init__(self,name,location,age):
        self.name = name
        self.location = location
        self.age = age
        self.login_attempts =3

    def describe_user(self):
        """Summarize the informaation collected."""
        print ("\nUser is " + self.name.title() + " who is " +
               str(self.age) + " years old and from " +
               self.location.title() + ".")

    def greet_user(self):
        """Simulate greeting user."""
        print ("\nHello " + self.name.title() + "!")
        print ("Thank you for joining our site from " +
               self.location.title() + ".")


    def increment_login_attempts(self,increment):
        """Allow users to inrease logins by 1."""
        self.login_attempts += increment

    def reset_login_attempt(self,reset):
        """Simulate that it returns the value of login attempts to 0."""
        self.login_attempts = reset

        if reset >= 1:
            self.login_attempts = 0

        else:
            print ("\nThe system has already been reset.")

    def read_attempts(self):
        """Summarize login."""
        print ("You have logged in " + str(self.login_attempts) + " times.")


class Admin(User):
    """Simulate link between child class and parent class."""

    def __init__(self,name,location,age):
        """Initialise attributes of the parent class."""
        super().__init__(name,location,age)

        #Initialise an empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    """Simulate listing of attributes of this class."""

    def __init__(self,privileges_list=[]):
        self.privileges_list = privileges_list

    def show_privileges(self):
        print ("\nPrivileges:")
        if self.privileges_list:
            for privilege in self.privileges_list:
                print("- " + privilege)
        else:
            print ("This user has no privileges!")



ken = Admin('ken fowler','chicago',35)
ken.describe_user()

ken.privileges.show_privileges()

print ("\n----Adding privileges----")

ken.privileges_list = ['can block users','can change script','can reset passwords']

ken.privileges.privileges_list = ken.privileges_list
ken.privileges.show_privileges()


#Ex 9-9
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


his_car = Electric_Car('mercedes','s class',2017)
print ("\n" + his_car.get_descriptive_name())

his_car.battery.describe_battery()
his_car.battery.get_range()

print ("\n ...Upgrading battery...")
print ("Battery upgrade complete!")

his_car.battery.upgrade_battery()
his_car.battery.describe_battery()
his_car.battery.get_range()