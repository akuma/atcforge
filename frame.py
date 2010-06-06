#coding=utf-8

import web

from template import render
from template import render_plain

urls = (
    '/?', 'Index',
    '/menu', 'Menu',
)

class Index:

    def GET(self):
        return render_plain.frame.frame()

class Menu:

    def GET(self):
        return render_plain.frame.menu()

class NotFound:

    def GET(self):
        return render.notFound()

app = web.application(urls, globals())
