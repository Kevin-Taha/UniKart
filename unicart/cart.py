from google.appengine.ext import ndb
from item import Item
class Cart(ndb.Model):
    name = ndb.StringProperty()
    budget = ndb.IntegerProperty()
    description = ndb.StringProperty()
    user = ndb.StringProperty()
    items = ndb.KeyProperty()
