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