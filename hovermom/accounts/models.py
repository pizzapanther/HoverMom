from google.appengine.ext import ndb

class Organization (ndb.Model):
  name = ndb.StringProperty(required=True)
  created = ndb.DateTimeProperty(auto_now_add=True)
  
class ApiKey (ndb.Model):
  akey = ndb.StringProperty()
  organization = ndb.KeyProperty(kind='Organization')
  active = ndb.BooleanProperty(default=True)
  created = ndb.DateTimeProperty(auto_now_add=True)
  
class User (ndb.Model):
  google_id = ndb.UserProperty()
  
  orgs = ndb.KeyProperty(kind='Organization', repeated=True)
  
  created = ndb.DateTimeProperty(auto_now_add=True)
  