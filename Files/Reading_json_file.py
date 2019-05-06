import json

filename = 'numbers.json'
with open(filename) as f_obj:
    read_file = json.load(f_obj)

print(read_file)

#Now reading another file that stored user data

filename2 = 'username.json'
with open(filename2) as user:
    user_info = json.load(user)
    print("Welcome back " + user_info + "!")
