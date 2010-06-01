#coding=utf-8

import web
import frame
import control
#import action
#import function
#import delegate

### Url mappings
urls = (
    '/', 'frame.Frame',
    '/menu', 'frame.Menu',
    '/control', 'control.Index',
    '/control/new', 'control.New',
    '/control/(.+)/del', 'control.Delete',
    '/control/(.+)', 'control.Edit',
    '/hello/(.+)', 'control.Hello',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
