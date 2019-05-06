import json

filename = 'location.json'
try:
    with open(filename) as f_obj:
        location = json.load(f_obj)
except FileNotFoundError:
    location = input("Where do you stay? ")
    with open(filename,'w') as f_obj:
        json.dump(location,f_obj)
        print ("We'll remember this next time!")
else:
    print("How is the weather in " + location + "?")

#This oens a new file location.json which didint exists and stores my input
#but if this file already exists it prints the last statement.