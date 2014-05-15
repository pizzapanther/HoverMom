
from google.appengine.ext import ndb

class Ping (ndb.Model):
  monitor = KeyProperty(kind='Monitor')
  timestamp = ndb.DateTimeProperty(auto_now_add=True)
  