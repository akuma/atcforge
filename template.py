#coding=utf-8

import web

### Templates
render = web.template.render('templates', base='base')
render_plain = web.template.render('templates')
