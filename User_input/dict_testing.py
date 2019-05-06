music_list = {}


while True:
    print("Album polls")
    print("Type exit to end program")

    artist = input("\nName of the musician: ")
    if artist == 'exit':
        break

    composed_album = input("Favorite album: ")
    music_list[artist] = composed_album
    if composed_album == 'exit':
        break

print ("\n----Poll Results----")

print (music_list)