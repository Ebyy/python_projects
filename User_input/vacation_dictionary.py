vacation_list = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    destination = input("Where would you like to spend your next vacation?")

    vacation_list[name] = destination

    ask = input("Would you like to continue with the poll? (Yes/No)")

    if ask == 'no':
        polling_active = False

print("\n----Poll Results-----")
for name,destination in vacation_list.items():
    print (name.title() + " would like to go to " + destination.title() + ".")


print (vacation_list)