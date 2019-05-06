from Users_class_module import User

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