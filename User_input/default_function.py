def describe_pet(pet_name,animal_type='dog'):
    print ("\nI have a " + animal_type + ".")
    print ("My " + animal_type + "'s name is " + pet_name.title() + ".")

#same out put is generated because the animal type is by default a dog.
describe_pet('rocky')
describe_pet(pet_name='lexy')

#when they generate same outputs they are called equivalent function calls.
describe_pet('willie')
describe_pet(pet_name='willie')

def make_shirt(text,size='XL'):
    print ("\nMy fav shirt is sized " + size + " and has a slogan "
           + text.title() + " written in front.")

make_shirt(text="'bold princess'")

def describe_city(city,country='Nigeria'):
    print ("\n" + city.title() + " is in " + country.title())

describe_city('lagos')
describe_city('paris')
describe_city('abuja')

#working with return

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('sean','carter')
print (musician)

husband = get_formatted_name('obi','ogunedo')
print(husband)

#to make a default value optional in a function call.
def get_full_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' +last_name
    return full_name.title()


musician = get_full_name('beyonce','knowles')
print(musician)

barber = get_full_name('sean','combs','diddy')
print(barber)

def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person

actor = build_person('hugh','jackman')
print(actor)

def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

actor = build_person('jamie','foxx',age=46)
print(actor)