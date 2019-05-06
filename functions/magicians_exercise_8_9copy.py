def show_magicians(magicians):
    """Print name of each magician"""
    for magician in magicians:
        print (magician)


def make_great(magicians):
    """add phrase the great to each"""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician.title() + " the Great"
        great_magicians.append(great_magician)

    #Add the great magicians back into magicians
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['dombledoor','lord varis','harry']
show_magicians(magicians)


print("\n")
make_great(magicians)
show_magicians(magicians)
