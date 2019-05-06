
num_list = [[5,8,10],[1,2,3],[11,22,33]]

for x in range(0,3):
    for y in range(0,3):
        print (num_list[x][y])

current_number = 1
while current_number <= 5:
    print (current_number)
    current_number += 1

prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print (message)

#to prevent quit from being printed...

prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print (message)