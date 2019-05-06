try:
    with open('C:/Users/Home/PycharmProjects/Classes/random_poll.txt') as f_object:
        poll_results = f_object.read()
except FileNotFoundError:
    message = 'Sorry, this file does not exist!'
    print(message)
else:
    """Count number of words in this file."""
    words = poll_results.split()
    #this sections each of the words in the file and stores it in a list.
    num_words = len(words)
    print("This file has " + str(num_words) + " words.")

print (words)