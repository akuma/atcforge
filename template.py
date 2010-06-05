#coding=utf-8

import web

### Templates
render = web.template.render('templates', base='layout/base')
render_plain = web.template.render('templates')
