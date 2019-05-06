class Restaurant():
    """Create attribute for the class using methods"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate a few descriptions."""
        print ("\n" + self.restaurant_name.title() +
               " is quite famous.")
        print ("It is mainly known for " + self.cuisine_type.title() +
               " cuisine.")

    def open_restaurant(self):
        """Simulate an annoucement"""
        print(self.restaurant_name.title() + " is now open for the evening.")



favorite_diner = Restaurant('the good son','chinese')
next_diner = Restaurant('dailo','french')
restaurant = Restaurant('callies','american')

print ("My favorite restaurant is " + favorite_diner.restaurant_name.title())
favorite_diner.describe_restaurant()
favorite_diner.open_restaurant()

print ("\nThe next one i like is " + next_diner.restaurant_name.title() + " restaurant.")
next_diner.describe_restaurant()
next_diner.open_restaurant()

restaurant.describe_restaurant()
restaurant.open_restaurant()

class Users():
    """Use methods to define."""

    def __init__(self, first_name, last_name,location,age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

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


first_user = Users('ed','james','toronto',25)
second_user = Users('adaku','okeke','lagos',19)
third_user = Users('andrea','garcia','madrid',37)

print ("\nSome information on our first client, " + first_user.first_name.title() +
       " " + first_user.last_name.title() + ".")
first_user.describe_user()
first_user.greet_user()

print ("\nSome information on our second user, " + second_user.first_name.title() + ".")
second_user.describe_user()
second_user.greet_user()

print ("\nSome information on our third client, " +
       third_user.last_name.title())
third_user.describe_user()
third_user.greet_user()