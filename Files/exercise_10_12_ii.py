import json

try:
    with open('favorite_number.json') as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    favorite_number = input("What is your favorite number?")
    with open('favorite_number.json', 'w') as f_object:
        json.dump(favorite_number, f_object)
        print("Thanks! I'll remember that.")
else:
    print("I know your favorite number! It is " + favorite_number + ".")
