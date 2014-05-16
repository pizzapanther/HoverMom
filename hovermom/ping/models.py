
from google.appengine.ext import ndb

class Ping (ndb.Model):
  monitor = ndb.KeyProperty(kind='Monitor', required=True)
  created = ndb.DateTimeProperty(auto_now_add=True)
  