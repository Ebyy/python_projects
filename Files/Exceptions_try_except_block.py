#python can't execute print (5/0) so a zero division error is given
#but one can work around this by giving users a more friendlier
#  feedback like a try-except block below

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#This can also be used to handle a FileNotFoundError

try:
    with open('random_poll.txt') as file_object:
        notes = file_object.read()
except FileNotFoundError:
    message = "Sorry, this file does not exist!"
    print (message)

