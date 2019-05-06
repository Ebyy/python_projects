print ("Enter 'q' or 'N' to quit!")

responses = []

while True:
    response = input("Why do you love programming: ")
    responses.append(response)

    if response == 'q':
        break

    continue_poll = input("Do you want someone else to answer - (Y/N)? ")
    if continue_poll == 'N':
        break
    else:
        with open('programming_poll.txt','a') as file_object:
            file_object.write(response + "\n")

with open('programming_poll.txt') as poll_results:
    results = poll_results.readlines()

for result in results:
    print(result.rstrip())