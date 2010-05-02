# coding=utf-8
import web

urls = (
    '/test', 'test',
    '/seeother', 'seeother',
    '/redirect', 'redirect',
    '/page1', 'page1',
    '/page2', 'page2',
    '/testdb', 'testdb',
    '/(.*)', 'hello',
)

db = web.database(dbn='sqlite', db='demodb')

app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class test:
    def GET(self):
        return '''<html>
          <head>
            <title>test page</title>
          </head>
          <body>
            <form action="seeother" method="post">
              <input type="submit" value="seeother test">
            </form>
            <br>
            <form action="redirect" method="post">
              <input type="submit" value="redirect test">
            </form>
          </body>
        </html>'''

class page1:
    def GET(self):
        return 'This is seeother page.'

class page2:
    def GET(self):
        return 'This is the redirect page.'

class seeother:
    def POST(self):
        # Do some application logic here, and then:
        raise web.seeother('/page1')

class redirect:
    def POST(self):
        # Do some application logic here, and then:
        raise web.redirect('/page2')

class testdb:
    def GET(self):
        print db.select('todo', where='id=1')
        return 'This is the db test page.'

if __name__ == "__main__":
    app.run()
