#For a function to use a random or arbitrary number of arguments (*) is placed before the value.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print (toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#We can even introduce a loop to this function

def make_icecream(*flavours):
    """Tell them what is in the icecream"""
    print ("\nThe ice-cream contains the following flavors: ")
    for flavour in flavours:
        print ("- " + flavour)

make_icecream('strawberry','vanilla')
make_icecream('coffee')
make_icecream('mango','orange','bubble gum')

#if random or arbitrary values are to be combined with either positional or keyword arguments,
#the arbitrary argument should be the final parameter in the set up.

def make_snack(size,*types):
    """Summarize the snack we are about to make."""
    print ("\nHaving a " + size +
           " sized snack that includes: ")
    for type in types:
        print ("- " + type)

make_snack('large','burger','fries')
make_snack('small','peanuts','popcorn','soda')

#Using Arbitrary keyword arguments
def build_profile(first,last,**user_info):
    """Build a dictionary with all the info at the end."""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',sex='male',field='science')
print(user_profile)

#Exercises

def make_sandwich(*stuffings):
    print ("\nHere is your sandwich with the "
           "following stuffing: ")
    for stuffing in stuffings:
        print ("- " + stuffing)

make_sandwich('chicken','pickles','mayo')
make_sandwich('cheese')
make_sandwich('cabbage','tomato slices','lettuce','tofu')


def make_car(manufacturer,model,**other_info):
    car_info = {}
    car_info['car_type'] = manufacturer
    car_info['model'] = model
    for key,value in other_info.items():
        car_info[key] = value

    return car_info

car = make_car('subaru','outback',color='blue',tow_package='True')
print (car)

dream_car = make_car('mercedes','G wagon',color='silver')
print (dream_car)