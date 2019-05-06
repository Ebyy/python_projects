#Filling a dictionary with user input

responses = {}

#flag
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which is you favorite fruit? ")

    responses[name] = response   #store name in dictionary

    #find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

#for results
print ("\n---Poll Results---")

for name,response in responses.items():
    print (name.title() + " would like one/some " + response + ".")


print (responses)