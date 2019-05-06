from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()
#this prompt python to creat an instance of OrderedDict class
# and store that instance in favorite languages
favorite_languages['jen'] = 'r'
favorite_languages['jack'] = 'python'
favorite_languages['simbi'] = 'java'
favorite_languages['musa'] = 'ruby'

for name,language in favorite_languages.items():
    print (name.title() + "'s favorite language is " + language.title() + ".")


print (OrderedDict())
print(favorite_languages)

x=randint(1,6)

class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        """Simulate rolling die to get a random number."""
        return randint(1,self.sides)

my_die = Die()

results = []

for roll_number in range(10):
    result = my_die.roll_die()
    results.append(result)

print ("\nResults of 10 rolls of a 6 sided die are as follows:")
print(results)

die = Die(sides=10)

results = []

for roll_number in range(10):
    result = die.roll_die()
    results.append(result)

print ("\nResults of 10 rolls of a 10-sided die are as follows:")
print(results)

die_20 = Die(sides=20)

results = []

for roll_number in range(10):
    result = die_20.roll_die()
    results.append(result)

print ("\nThe results of a 20-sided die rolled 10 times:")
print (results)