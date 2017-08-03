#!/usr/bin/env python
# -*- coding: utf-8 -*-﻿
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
from google.appengine.api import users
from cart import Cart
from item import Item
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
##################################################################
#Handlers Start Here
##################################################################
class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template("templates/mainPage.html")
        self.response.write(my_template.render())
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = '''Welcome, {}! (
            <a href="{}">
            If that's not you, sign out)
            </a>
            <a href = "userPage">
            </br>
             <h1> Continue to the Main Page </h1>
            </a>
            '''.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/userPage')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write('<html><body>{}</body></html>'.format(greeting))
class AboutHandler(webapp2.RequestHandler):
        def get(self):
            my_template = jinja_environment.get_template("templates/aboutPage.html")
            self.response.write(my_template.render())
class UserPageHandler(webapp2.RequestHandler):
        def get(self):
            my_template = jinja_environment.get_template("templates/userPage.html")
            current_user = users.get_current_user()
            nickname = current_user.nickname()
            render_data = {
                'username' : nickname,
            }

            cartlist = Cart.query(Cart.userId == current_user.user_id()).fetch()
            render_dict = {}
            render_data["cartlist"] = cartlist
            self.response.write(my_template.render(render_data))


class ListHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        my_template = jinja_environment.get_template("templates/listPage.html")
        cartName = self.request.get("cartname")
        cartBudget = self.request.get("budget")
        if cartBudget == "":
            cartBudget = 0
        cartDesc = self.request.get("desc")
        myCart = Cart(name = cartName,
                      budget = int(cartBudget),
                      description = cartDesc,
                      user = nickname,
                      userId = user.user_id())
        if cartName != "":
            myCart.put()
            self.redirect("userPage")
        self.response.write(my_template.render())


class ViewHandler(webapp2.RequestHandler):
        def get(self):
            my_template = jinja_environment.get_template("templates/view.html")
            itemname = self.request.get("name")
            itemtag = self.request.get("tag")
            itemprice = self.request.get("price")
            if itemprice == "":
                itemprice = 0
            itemurl = self.request.get("url")
            itemquantity = self.request.get("quantity")
            itempriority = self.request.get("priority")
            cart_name = self.request.get("cartname")
            if itemquantity == "":
                itemquantity = 1
            my_item = Item(itemname = itemname, url = itemurl, price = int(itemprice), tag = itemtag, quantity = int(itemquantity), priority = itempriority)
            if itemname != "":
                query = Item.query()
                results = query.fetch()
                usedList = []
                for i in range(len(results)):
                    url = results[i].url
                    if url not in usedList:
                        usedList.append(url)
                if itemurl not in usedList:
                    my_item.put()
            itemlist = Item.query(Item.itemname != "").fetch()
            total = 0;
            for item in itemlist:
                total += item.price
            render_data = {
            "itemlist" : itemlist,
            "total" : total
            }

            self.response.write(my_template.render(render_data))


##################################################################
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/about', AboutHandler),
    ('/userPage', UserPageHandler),
    ('/lists', ListHandler),
    ('/view', ViewHandler),
], debug=True)
