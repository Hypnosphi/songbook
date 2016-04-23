from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<slug>[^/]+)$', views.view_gig, name='view-gig'),
    url(r'^(?P<slug>[^/]+)/edit$', views.edit_gig, name='edit-gig'),
    url(r'^(?P<slug>[^/]+)/add-comment$',
        views.add_gig_comment, name='add-gig-comment'),
    url(r'^add-song-comment/(?P<song_id>\d+)$',
        views.add_song_comment, name='add-song-comment'),
]
