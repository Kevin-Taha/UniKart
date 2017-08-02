from google.appengine.ext import ndb

class Cart(ndb.Model):
    name = ndb.StringProperty()
    budget = ndb.IntegerProperty()
    description = ndb.StringProperty()
    items = ndb.KeyProperty()
