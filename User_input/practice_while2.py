sandwich_options = ['chicken','turkey','pastrami','cheese','veggie',
                    'tuna','turkey','cheese','turkey','cola','juice']
my_order = []

while 'turkey' in sandwich_options:
    sandwich_options.remove('turkey')

print (sandwich_options)

ordering = True
while ordering:
    prompt = input("What can I get you? ")
    request = sandwich_options.pop()

    my_order.append(request)

    prompt2 = input("Is that all? (yes/no)")
    if prompt2 == 'yes':
        ordering = False
        print ("\nYour order is ready for collection: ")
        for order in my_order:
            print ("\t" + order)
        break