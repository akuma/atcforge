#coding=utf-8

"""run.py"""

import web
import control
#import action
#import function
#import delegate

### Url mappings
urls = (
    '/', 'control.Frame',
    '/menu', 'control.Menu',
    '/control', 'control.Index',
    '/control/new', 'control.New',
    '/control/(.+)/del', 'control.Delete',
    '/control/(.+)', 'control.Edit',
    '/hello/(.+)', 'control.Hello',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
