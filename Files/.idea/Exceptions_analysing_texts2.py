filename = 'C:/Users/Home/PycharmProjects/Files/chapter 10/alice.txt'

def count_words(filename):
    """Count number of words in this file."""
try:
    with open(filename) as f_object:
        poll_results = f_object.read()
except FileNotFoundError:
    message = 'Sorry, this file does not exist!'
    print(message)
else:
    words = poll_results.split()
    # this sections each of the words in the file and stores it in a list.
    num_words = len(words)
    print("This file has " + str(num_words) + " words.")


#For this to work as a function we have to move the whole commands
#  into the body of the function like in the next script

def counting_words(filename):
    """Count number of words in this file."""
    try:
        with open(filename) as f_object:
            poll_results = f_object.read()
    except FileNotFoundError:
        message = 'Sorry, this file does not exist!'
        print(message)
    else:
        words = poll_results.split()
        # this sections each of the words in the file and stores it in a list.
        num_words = len(words)
        print("This file has " + str(num_words) + " words.")

#Now call the script
counting_words(filename)