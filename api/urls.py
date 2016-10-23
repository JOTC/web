from django.conf.urls import url

from .endpoints import shows

urlpatterns = [
    url(r'^shows/?$', shows.get, name='shows.get'),
]
