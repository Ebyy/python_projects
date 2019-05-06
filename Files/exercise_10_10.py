def count_words(filename):
    """Initialise function to help analyse files."""
    try:
        with open(filename) as file_content:
            contents = file_content.read()
    except FileNotFoundError:
        pass
    else:
        the_count = contents.count('the')
        print ("\nThe number of 'the' in this file is " + str(the_count))
        x_the_count = contents.lower().count('the')
        print ("The exact number of 'the' in this file is " + str(x_the_count))

filenames = ['C:/Users/Home/PycharmProjects/Files/chapter 10/alice.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/moby_dick.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/little_women.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/siddhartha.txt',
             'C:/Users/Home/PycharmProjects/Files/chapter 10/python_notes.txt']

for filename in filenames:
    count_words(filename)