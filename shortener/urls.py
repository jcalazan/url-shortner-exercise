from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from web.views import go, shorten


urlpatterns = patterns('',
    url(r'^$', shorten),
    url(r'^web/', include('web.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^.*/?$', go),
)