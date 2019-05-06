tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print ("I am 6'2\" tall.")
print ('I am 6\'2" tall.')

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print (x)
print (y)

print ("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print (w + e)

print ("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print ("." * 10) #whatt did that do

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter,formatter))
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print ("Here are the days: ", days)
print ("Here are the months: ", months)

print ("""
There is something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

print ('''How is this working?
I absolutely want to know.
i have to understand the steps to be able to learn.
That's all for now.''')

from sys import argv

