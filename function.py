#coding=utf-8

import web
import action_model
import function_model
from template import render

urls = (
    '/a/(.+)', 'Index',
    '/new/(.+)', 'New',
    '/(.+)', 'Edit',
)

def func_form():
    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull, description='功能名称'),
        web.form.Dropdown('state', [('1', '正常'), ('0', '废弃')], web.form.notnull, description='功能状态'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton')
    )
    return form

class Index:

    def GET(self, action_id):
        functions = function_model.get_functions(action_id)
        return render.function.functionList(functions)

class New:

    def GET(self, action_id):
        form = func_form()
        return render.function.functionNew(form)

    def POST(self, action_id):
        form = func_form()

        if not form.validates():
            return render.function.functionNew(form)

        function_model.new_function(action_id, form.d.name, form.d.state, form.d.description)
        raise web.seeother('/')

class Edit:

    def GET(self, id):
        form = func_form()
        function = function_model.get_function(id)
        form.fill(function)
        return render.function.functionEdit(form)

    def POST(self, id):
        form = func_form()

        if not form.validates():
            return render.function.functionEdit(form)

        function_model.update_function(id, form.d.name, form.d.state, form.d.description)
        raise web.seeother('/')

class Delete:

    def GET(self, id):
        function_model.del_function(id)
        raise web.seeother('/')

app = web.application(urls, globals())
