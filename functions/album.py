def make_album(artist,song_title):
    """create the dictionary containing artist and song title"""
    album = {'singer':artist,'song':song_title}
    return album

fav_album = make_album('celine dion','a new day has come')
print (fav_album)


def make_album(artist,song_title,tracks=''):
    """This leaves room for the tracks incase that is provided."""
    album = {'singer':artist,'song':song_title}
    if tracks:
        album['tracks'] = tracks
    return album

fav_album = make_album('celine dion','a new day has come',tracks=14)
print (fav_album)


def make_album(artist,album,tracks,location=''):
    """Default location left empty so it can be filled."""
    album = {'musician':artist,'album_title':album,'number of tracks':tracks}
    if location:
        album['country'] = location
    return album

download = make_album('jay z','4:44','12',location='america')
print ("\nThe details in my downloads:")
print (download)