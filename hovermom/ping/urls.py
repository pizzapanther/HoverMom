from django.conf.urls import patterns, url

urlpatterns = patterns('ping.views',
  url(r'^tasks/check-pings$', 'check_pings', name='task-check-pings'),
  url(r'^$', 'ping', name='ping'),
)
