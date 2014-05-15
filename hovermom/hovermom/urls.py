from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  # url(r'^$', 'hovermom.views.home', name='home'),
  url(r'^ping/', include('ping.urls')),
)
