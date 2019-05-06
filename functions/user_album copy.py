def make_album(artist,album_title):
    album_dict = {'artist':artist.title(),'album_title':album_title.title()}
    return album_dict

print ("Enter 'q' to quit poll. ")

while True:
    artist = input("\nWho is your favorite artist? ")
    if artist == 'q':
        break
    album_title = input("Which album do you like best? ")
    if album_title == 'q':
        break

    album = make_album(artist,album_title)
    print (album)

print ("Thanks for participating in our poll.")