import json

def get_stored_username():
    """Get stored username."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    filename = 'username.json'
    username = input("What is your username?")
    with open(filename,'w') as file_obj:
        json.dump(username,file_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you next time you come back " + username + "!")

greet_user()