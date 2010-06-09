#coding=utf-8

import web
import frame
import product
import action
import function
import control

### Url mappings
urls = (
    # frame module
    '/frame', frame.app,

    # product module
    '/product', product.app,

    # action module
    '/action', action.app,

    # function module
    '/function', function.app,

    # control module
    '/control', control.app,

    # 404 page
    '.+', 'frame.NotFound'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
