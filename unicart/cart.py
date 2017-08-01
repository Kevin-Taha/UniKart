from google.appengine.ext import ndb

class Cart(ndb.Model):
    name = ndb.StringProperty()
    budget = ndb.IntegerProperty()
    items = ndb.KeyProperty()
