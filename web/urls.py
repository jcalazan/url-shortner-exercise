from django.conf.urls import patterns, url

from .views import shorten, go


urlpatterns = patterns('',
       url(
           regex=r'^shorten/',
           view=shorten,
           name='shorten'
       ),
)