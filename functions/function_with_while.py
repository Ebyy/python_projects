def get_full_name(first_name,last_name):
    full_name = first_name + ' ' +last_name
    return full_name.title()

while True:
    print ("\nPlease tell me your name: ")
    print ("Enter 'q' at anytime to quit.")

    first_name = input("First name: ")
    if first_name == 'q':
        break

    last_name = input("Last name: ")
    if last_name == 'q':
        break

    formatted_name = get_full_name(first_name,last_name)
    print ("\nHello " + formatted_name + "!")