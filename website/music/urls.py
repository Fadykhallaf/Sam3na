"""this is urls of music app"""
from django.conf.urls import url
from music import views

app_name = "music"
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^register/^$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # music/album/album_id
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # music/album/album_id/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]