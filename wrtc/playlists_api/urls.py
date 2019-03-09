from django.conf.urls import url

from playlists_api import views

urlpatterns = [
    url(r'^all/(?P<username>.+)$', views.PlaylistView.as_view()),
]
