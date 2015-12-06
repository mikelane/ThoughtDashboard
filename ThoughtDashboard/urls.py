from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ThoughtDashboard.views.index', name='index'),
    url(r'^details/$', 'ThoughtDashboard.views.details', name='details'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
