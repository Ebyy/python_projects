import json

def guess_favorite_number():
    """Guess favorite user's number."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        favorite_number = input("What is your favorite number?")
        filename = 'favorite_number.json'
        with open(filename,'w') as f_object:
            json.dump(favorite_number,f_object)
            print("Thanks! I'll remember that.")
    else:
        print("I know your favorite number! It is " + favorite_number + ".")


guess_favorite_number()