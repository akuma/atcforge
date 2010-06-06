#coding=utf-8

import web
import control_model
from template import render

urls = (
    '/?', 'Index',
    '/new', 'New',
    '/(.+)/del', 'Delete',
    '/(.+)', 'Edit'
)

class Index:

    def GET(self):
        controls = control_model.get_controls()
        return render.index(controls)

class New:

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull, description='文件名称', class_='titleTd'),
        web.form.Dropdown('encoding', ['UTF-8', 'GBK'], web.form.notnull, description='文件编码'),
        web.form.Dropdown('is_enable', ['YES', 'NO'], web.form.notnull, description='是否启用'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton'),
    )

    def GET(self):
        form = self.form()
        return render.controlNew(form)

    def POST(self):
        form = self.form()

        if not form.validates():
            return render.controlNew(form)

        control_model.new_control(form.d.name, form.d.encoding, form.d.is_enable, form.d.description)
        raise web.seeother('/control')

class Edit:

    def GET(self, id):
        control = control_model.get_control(id)
        form = New.form()
        form.fill(control)
        return render.controlEdit(form)

    def POST(self, id):
        form = New.form()

        if not form.validates():
            return render.controlEdit(form)

        control_model.update_control(id, form.d.name, form.d.encoding, form.d.is_enable, form.d.description)
        raise web.seeother('/control')

class Delete:

    def GET(self, id):
        control_model.del_control(id)
        raise web.seeother('/control')

app = web.application(urls, globals())
