with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

#3 different ways to read the file

with open ('python_notes.txt') as file_object:
    lessons = file_object.read()

print (lessons.rstrip())


with open ('python_notes.txt') as file_object:
    for line in file_object:
        print(line)


with open('python_notes.txt') as notes:
    lines = notes.readlines()

for line in lines:
    print(line)


#To replace a prase in the document, this is done :

with open('python_notes.txt') as file_object:
    notes = file_object.read()

print (notes.replace('python','ruby'))


#to print from a folder the entire file path has to be quoted like done below

with open('C:/Users/Home/PycharmProjects/Files/chapter 10/alice.txt') as trial:
    trials = trial.read()

print(trials)