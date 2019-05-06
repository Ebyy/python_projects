def make_album(music_artist,composed_album):
    music_list = {'music_artist': music_artist.title(), 'composed_album': composed_album.title()}
    return music_list

while True:
    print("\nAlbum polls")
    print("Type 'exit' to end program")

    music_artist = input("\nName of the musician: ")
    if music_artist == 'exit':
        break

    composed_album = input("Favorite album: ")
    if composed_album == 'exit':
        break

    user_album = make_album(music_artist, composed_album)
    print (user_album)

print ("Thanks for taking part in our poll.")





