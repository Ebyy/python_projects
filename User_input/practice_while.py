ask = "\nWhat can I get you?"

order_list = []

filling_order = True

while filling_order:
    request = input(ask)

    order_list.append(request)

    repeat =  input("Would you like anything else? (Yes/No)")
    if repeat == 'no':
        filling_order = False

print ("\nYour order is ready and it contains: ")
for item in order_list:
    print("\t" + item.title())



