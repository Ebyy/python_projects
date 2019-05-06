print("If you enter two digits I can give you their sum.")
print ("Enter 'q' to quit!\n")

while True:
    try:
        num_1 = input("Please enter first number: ")
        if num_1 == 'q':
            break

        num_1 = int(num_1)

        num_2 = input("Please enter second number: ")
        if num_2 == 'q':
            break

        num_2 = int(num_2)

    except ValueError:
        error_msg = "Sorry, the value you entered is not a valid number."
        print(error_msg)
    else:
        answer = num_1 + num_2
        print ("The sum of " + str(num_1) + " and " + str(num_2) + " is " + str(answer))