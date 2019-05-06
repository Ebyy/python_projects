import json

def get_stored_username():
    """Get stored username."""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    """Greet user by username."""
    username = get_stored_username()
    if username:
        print ("Welcome back " + username +"!")
    else:
        username = input("What is your username?")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back" + username + "!")

greet_user()