from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloud_kelp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.trending', name='trending'),
    url(r'results/(?P<query>\w+)/$', 'website.views.results', name='results'),
    url(r'details/(?P<query>\w+)/$', 'website.views.details', name='details'),
)