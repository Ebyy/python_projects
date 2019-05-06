prompt = "How old are you?"
prompt += "\nEnter 'end' to exit. "

answer = ""
'end'==False
while True:
    answer = input(prompt)
    age = int(answer)

    if age <= 3:
        print("Free ticket")
    elif age > 12:
        print("$15")
    else:
        print("$10")



