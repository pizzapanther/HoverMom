import datetime
import logging

from django import http
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from google.appengine.ext import ndb
from google.appengine.api import mail

from accounts.models import ApiKey
from monitor.models import Monitor
from ping.models import Ping

@csrf_exempt
def ping (request):
  akey = request.REQUEST.get('key', '')
  mstr = request.REQUEST.get('monitor', '')
  
  apiKey = ApiKey.query(ApiKey.akey == akey).get()
  if apiKey:
    mkey = ndb.Key(urlsafe=mstr)
    monitor = mkey.get()
    if mkey.kind() == 'Monitor' and monitor:
      if apiKey.organization.urlsafe() == monitor.organization.urlsafe():
        ping = Ping(monitor=mkey)
        ping.put()
        
        return http.HttpResponse('So long and thanks for all the fish!', content_type='text/plain')
        
  raise http.Http404
  
def check_pings (request):
  for monitor in Monitor.query(Monitor.active == True).fetch():
    now = datetime.datetime.utcnow()
    old = now - datetime.timedelta(minutes=6)
    
    ping = Ping.query(Ping.created >= old).get()
    kw = {
      'name': monitor.name,
      'key': monitor.key.urlsafe(),
      'ts': now.strftime("%m/%d/%Y %H:%M UTC")
    }
    
    if ping:
      logging.info('Ping Good: {name} {key}'.format(**kw))
      
    else:
      logging.info('Ping Missing: {name} {key}'.format(**kw))
      mail.send_mail(
        settings.DEFAULT_FROM_EMAIL,
        settings.PING_REPORT_EMAIL,
        '"{name}" failed to report - {ts}'.format(**kw),
        'Monitor "{name}" failed to report in the last 5 minutes.\n\n'.format(**kw)
      )
      
  return http.HttpResponse('OK', content_type='text/plain')
  