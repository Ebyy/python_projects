print ("The following are lists of magicians: ")

def show_magician(names):
    """Print out list of magicians"""
    for name in names:
        print (name.title())

magicians = ['dombledoor','lord varis','harry']
show_magician(magicians)


