#lists
#locating items or citing in a list using listname[0,1,... or -1to start from the back]
#editing using upper,lower&title()...then concatenation of strings,note that the variable need to be defined b4 use
#adding stuff to a list list_name.append('dggh') is used while ...
# with .insert(-3,'dhd') for specific position and item
#.remove(item) or del list_name(3) for removing items
#.pop() is used to single out or pick an item from the list ...
#..but when used as seen it refers to the last item on the list
#working with range
for value in range(1,11):
    print (value)
numbers = list(range(1,11))
print (numbers)
odd_numbers = list(range(1,11,2))
#so this checks numbers starting from 1 and ending before 11 (10)
# and adds 2 to the number hence giving the next value
print (odd_numbers)
for thirds in range(3,30,3):
    print (thirds)

#To copy a list a slice[:] is very important.
#Don't equate! because that just reassigns the value
my_colours = ['red','blue','yellow']
your_colours = my_colours[:]    #instead of your_colours = my_colours

#Tuples on the other hand are used to make lists that cant easily be changed. () is used instead of []
#They can be modified thus
line = (28,30)

print ("Original line:")
for line_point in line:
    print (line_point)

line = (25,33)
print("\nModified line:")
for line_point in line:
    print (line_point)

food_options = ('fried chicken', 'rice', 'beans', 'stew')
print ("Tonight's buffet includes:")
for food in food_options:
    print (food)

food_options = ('duck', 'potatoes', 'soup')
print ("\nWhile tomorrow's menu lists:")
for food in food_options:
    print(food)

#Dictionary
#dictionary_name[pair]=item_other eg alien['color'] = 'white' is used to add things to a dictionary
alien_2 = {} #started with an empty dictionary and built it up.
alien_2['color'] = 'blue'
alien_2['points'] = 3
print (alien_2)

favorite_number = {}
favorite_number['jen'] = 10
favorite_number['egan'] = 27
print(favorite_number)

#OR you can just do this

vacation_spots = {
    'ann':'paris',
    'bonny':'venice',
    'mike':'fiji',
    'drew':'lagos'
    }

#looping through dictionaries
for k,v in vacation_spots.items():   #with k and v repping variables.... if loops can be used too
    print ("\nKey: " + k)
    print ("Value: " + v)

#while loop is tricky because it continues so long as the condition stated earlier remains true
#except another condition is used to break it or turns returns false to the stated condition.