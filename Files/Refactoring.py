import json

filename = 'username.json'
def greet_user():
    """Initiate code to greet user."""
    try:
        with open(filename) as f_object:
            username = json.load(f_object)
    except FileNotFoundError:
        username = input("What is your username? ")
        with open(filename,'w') as f_object:
            json.dump(username,f_object)
            print("We'll remember you next time!")
    else:
        print("Welcome back " + username + "!")

greet_user()