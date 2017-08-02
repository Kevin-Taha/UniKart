from google.appengine.ext import ndb

class Item(ndb.Model):
    itemname = ndb.StringProperty()
    url = ndb.StringProperty()
    price = ndb.IntegerProperty()
    tag = ndb.StringProperty()
    quantity = ndb.IntegerProperty()
