from .models import Album
from django.shortcuts import render, get_object_or_404


def index(request):
    all_albums = Album.objects.all()

    context = {'all_albums': all_albums, }

    return render(request,'music/index.html',context)


def detail(request, album_id):

    #  album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album, })
