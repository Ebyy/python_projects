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

filenames = ['C:/Users/Home/PycharmProjects/Files/chapter 10/alice.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/moby_dick.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/little_women.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/siddhartha.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/python_notes.txt']

for filename in filenames:
    count_words(filename)

#This way, one can work on multiple files using the function.
#Notice how with the file Siddhartha,txt moved to classes the script still works.
#Within the function, the EXCEPT part can be altered with PASS -
    # This signals the script to FAIL SILENTLY with no notice given