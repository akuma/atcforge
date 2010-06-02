#coding=utf-8

import web
import model
from template import render

class Index:

    def GET(self, action_id):
        functions = model.get_functions(action_id)
        return render.functionList(functions)

class New:

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull, description='名称', class_='titleTd'),
        web.form.Dropdown('is_enable', ['YES', 'NO'], web.form.notnull, description='是否启用'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton'),
    )

    def GET(self):
        form = self.form()
        return render.functionNew(form)

    def POST(self):
        form = self.form()

        if not form.validates():
            return render.functionNew(form)

        model.new_function(form.d.name, form.d.is_enable, form.d.description)
        raise web.seeother('/function')

class Edit:

    def GET(self, id):
        function = model.get_function(id)
        form = New.form()
        form.fill(function)
        return render.functionEdit(form)

    def POST(self, id):
        form = New.form()

        if not form.validates():
            return render.functionEdit(form)

        model.update_function(id, form.d.name, form.d.is_enable, form.d.description)
        raise web.seeother('/function')

class Delete:

    def GET(self, id):
        model.del_function(id)
        raise web.seeother('/function')
