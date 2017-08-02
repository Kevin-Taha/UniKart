from google.appengine.ext import ndb
from cart import Cart

class Item(ndb.Model):
    itemname = ndb.StringProperty()
    url = ndb.StringProperty()
    price = ndb.IntegerProperty()
    tag = ndb.StringProperty()
    quantity = ndb.IntegerProperty()
    priority = ndb.StringProperty()
    incart = ndb.KeyProperty()
