from google.appengine.ext import ndb

class List(ndb.Model):
    title = ndb.StringProperty()
    name = ndb.StringProperty()
    url = ndb.StringProperty()
    price = ndb.IntegerProperty()
    tag = ndb.StringProperty()
