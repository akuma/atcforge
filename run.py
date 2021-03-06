#coding=utf-8

import web
import frame
import control
import action
import function

### Url mappings
urls = (
    '/hello/(.+)', 'control.Hello',
    # frame module
    '/', 'frame.Frame',
    '/menu', 'frame.Menu',
    # control module
    '/control', 'control.Index',
    '/control/new', 'control.New',
    '/control/(.+)/del', 'control.Delete',
    '/control/(.+)', 'control.Edit',
    # action module
    '/action', 'action.Index',
    '/action/new', 'action.New',
    '/action/(.+)/del', 'action.Delete',
	'/action/(.+)/fun', 'function.Index',
    '/action/(.+)', 'action.Edit',
    #'/function/new', 'function.New',
    #'/function/(.+)/del', 'function.Delete',
    #'/function/(.+)', 'function.Edit',	
    # 404 page
    '.+', 'frame.NotFound'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
