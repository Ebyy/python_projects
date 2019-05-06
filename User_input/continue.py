current_number = 0
while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print (current_number)

#Exercises
prompt = "Please enter what topping you would like: "
prompt += "\nEnter 'quit' when you are done. "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print (topping.title() + " added.")

