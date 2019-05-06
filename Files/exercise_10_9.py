#Tasked to show a script failing silently
print ("Types of dogs: ")

try:
    with open('C:/Users/Home/PycharmProjects/Files/dogs.txt') as dog_list:
        contents = dog_list.read()
except FileNotFoundError:
    error_message = "Sorry, this file does not exist."
    print (error_message)
else:
    print(contents.rstrip())

print ("\nTypes of cats: ")

try:
    with open('Cats.txt') as cat_list:
        cats = cat_list.read()
except FileNotFoundError:
    pass
else:
    print(cats.rstrip())