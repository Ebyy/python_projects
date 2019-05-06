from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# from django.shortcuts import render -was there before

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums}
    # render can be imported from shortcuts and used to run this
    # code too instead of using the template loader function
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})




        #html = ''
   # for album in all_albums:
        #url = '/music/' + str(album.id) + '/'
        #html += '<a href="' + url + '">' + album.album_title + '</a><br>'