from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<song_id>\d+)$', views.view_song, name='view-song'),
    url(r'^(?P<song_id>\d+)/remove$', views.remove_song, name='remove-song'),
    url(r'^(?P<song_id>\d+)/edit$', views.edit_song, name='edit-song'),
    url(r'^(?P<song_id>\d+)/copy$', views.copy_song, name='copy-song'),

    url(r'^(?P<song_id>\d+)/add-part$', views.add_song_part,
        name='add-song-part'),
    url(r'^part/(?P<part_id>\d+)/join$', views.join_song_part,
        name='join-song-part'),
    url(r'^part/(?P<part_id>\d+)/performer-(?P<performer_id>\d+)/kick$',
        views.kick_from_song_part, name='kick-from-song-part'),
    url(r'^part/(?P<part_id>\d+)/remove$', views.remove_song_part,
        name='remove-song-part'),

    url(r'^(?P<song_id>\d+)/add-link$', views.add_song_link,
        name='add-song-link'),
    url(r'^link/(?P<link_id>\d+)/edit$', views.edit_song_link,
        name='edit-song-link'),
    url(r'^link/(?P<link_id>\d+)/remove$', views.remove_song_link,
        name='remove-song-link'),

    url(r'^(?P<song_id>\d+)/watch-unwatch$', views.watch_unwatch_song,
        name='watch-unwatch-song'),
    url(r'^(?P<song_id>\d+)/mark-as-seen$', views.mark_song_as_seen,
        name='mark-song-as-seen'),

    url(r'^suggest/(?P<gigslug>[^/]+)$', views.suggest_a_song,
        name='suggest-song'),
]
