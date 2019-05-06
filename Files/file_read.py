with open('pi_30_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

with open('chapter 10/alice.txt') as file_object:
    findings = file_object.read()

print(findings.rstrip())

with open('chapter 10/pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_strings = ''
for line in lines:
    pi_strings += line.strip()

birthday = input('\nPlease enter your birthday like this ddmmyy: ')
if birthday in pi_strings:
    print ('Your birthday is in the first million digits of pi.')
else:
    print ("Your birthday isn't in the first million digits of pi.")

