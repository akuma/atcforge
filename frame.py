#coding=utf-8

from template import render
from template import render_plain

class Frame:

    def GET(self):
        return render_plain.frame()

class Menu:

    def GET(self):
        return render_plain.menu()

class NotFound:

    def GET(self):
        return render.notFound()
