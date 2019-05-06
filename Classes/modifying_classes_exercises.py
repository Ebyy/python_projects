class Restaurant():
    """Create attribute for the class using methods"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Simulate a few descriptions."""
        print ("\n" + self.restaurant_name.title() +
               " is quite famous.")
        print ("It is mainly known for " + self.cuisine_type.title() +
               " cuisine.")

    def open_restaurant(self):
        """Simulate an annoucement"""
        print(self.restaurant_name.title() + " is now open for the evening.")

    def set_number_served(self,number_served):
        """Simulate setting the number served."""
        self.number_served = number_served

    def increament_number_served(self,additional_number):
        """Initialize to allow the number of people served to be increaed."""
        self.number_served += additional_number


restaurant = Restaurant('Dominos','italian')
print ("The " + restaurant.restaurant_name + " served " +
       str(restaurant.number_served) + " number of people this evening.")

restaurant.number_served = 30
print ("The " + restaurant.restaurant_name + " served " +
       str(restaurant.number_served) + " number of people this evening.")

restaurant.set_number_served(50)
print ("The " + restaurant.restaurant_name + " served " +
       str(restaurant.number_served) + " number of people this evening.")

restaurant.increament_number_served(58)
print ("The " + restaurant.restaurant_name + " had to serve " +
       str(restaurant.number_served) + " people this evening.")



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
        print ("User is " + self.first_name.title() +
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


first_user = Users('dave','patterson','hamilton',14)

first_user.increment_login_attempts(1)
first_user.read_attempts()

first_user.reset_login_attempt(78)
first_user.read_attempts()
