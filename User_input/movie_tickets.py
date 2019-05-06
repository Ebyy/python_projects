prompt = "How old are you?"
prompt += "\nEnter 'end' to exit. "

active = True
while active:
    answer = input(prompt)

    if answer == 'end':
        active = False
        break

    if int(answer) <= 3:
        print ("Free ticket")
    elif int(answer) > 12:
        print ("$15")
    else:
        print ("$10")

