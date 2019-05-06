

while True:
    """Initialise filling prompt for guest list."""
    guest = input("Please enter guest name: ")

    if guest == 'q':
        break
    else:
        with open('guests.txt','a') as file_object:
            file_object.write(guest + "\n")


with open('guests.txt') as file_object:
    names = file_object.read()

print(names)