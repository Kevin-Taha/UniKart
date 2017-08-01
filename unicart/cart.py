from google.appengine.ext import ndb

class Cart(ndb.Model):
    name = ndb.StringProperty()
