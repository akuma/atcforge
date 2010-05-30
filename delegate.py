#coding=utf-8

"""delegate.py"""

import web
import types
import model

def delegate_apps(mapping):
    """Delegates appropriate app based on prefix.
       `mapping` should be tuple of (prefix, urls, fvars). """

    def f():
        for prefix, urls, fvars in mapping:
            if type(fvars) == types.ModuleType:
                fvars = fvars.__dict__

            if web.ctx.path.startswith(prefix):
                path = web.ctx.path[len(prefix):]

                # it will be better if web.request.handle takes path also as argument.
                # return web.request.handle(mapping, fvars, path)

                web.ctx.path = path
                return web.request.handle(urls, fvars)
        else:
            return web.notfound()

    return f

def run(mapping):
    """Starts web.py server with the specified mapping.
    `mapping` should be tuple of (prefix, urls, fvars).
    """
    handler = delegate_apps(mapping)
    web.run(handler, globals())
