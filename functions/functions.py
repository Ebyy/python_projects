def greet_user():
    """Display a simple greeting."""
    print ("Hello!")

greet_user()

def greet_user(username):
    print ("Hello " + username.title() + "!")

greet_user('sarah')

def display_message(chapter):
    print ("Currently learning about " + chapter + ".")

display_message('fuctions')

def favorite_book(book_title):
    print ("My favorite book is " + book_title.title() + ".")

favorite_book('mirror mirror')

def describe_pet(animal_type,pet_name):
    print ("\nI have a " + animal_type + ".")
    print ("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat','patty')
describe_pet('dog','renzo')

#Now above we used positional but sometime that can be confusing
# if the values are misplaced so to avoid that we can specify using keywords.

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='benny',animal_type='dog')