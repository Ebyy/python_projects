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