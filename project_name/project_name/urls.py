from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from home.views.index import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
