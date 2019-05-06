while True:
    """Initialise filling prompt for guest list."""
    guest = input("Please enter guest name: ")

    if guest == 'q':
        break
    else:
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(guest + " visited us.\n")
        print("Welcome " + guest + "! You have been added to the guest book. \n")


with open('guest_book.txt') as file_object:
    visitors = file_object.read()

print(visitors)
