from google.appengine.ext import ndb

class Monitor (ndb.Model):
  name = ndb.StringProperty(required=True)
  organization = ndb.KeyProperty(kind='Organization', required=True)
  active = ndb.BooleanProperty(default=True)
  
  created = ndb.DateTimeProperty(auto_now_add=True)
  