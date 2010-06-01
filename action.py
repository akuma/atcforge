#coding=utf-8


import web
import model
from template import render

class Index:

    def GET(self):
        actions = model.get_actions()
        return render.actionList(actions)

class New:

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull, description='名称', class_='titleTd'),
        web.form.Dropdown('is_enable', ['YES', 'NO'], web.form.notnull, description='是否启用'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton'),
    )

    def GET(self):
        form = self.form()
        return render.actionNew(form)

    def POST(self):
        form = self.form()

        if not form.validates():
            return render.actionNew(form)

        model.new_action(form.d.name, form.d.is_enable, form.d.description)
        raise web.seeother('/action')

class Edit:

    def GET(self, id):
        action = model.get_action(id)
        form = New.form()
        form.fill(action)
        return render.actionEdit(form)

    def POST(self, id):
        form = New.form()

        if not form.validates():
            return render.actionEdit(form)

        model.update_action(id, form.d.name, form.d.is_enable, form.d.description)
        raise web.seeother('/action')

class Delete:

    def GET(self, id):
        model.del_action(id)
        raise web.seeother('/action')

class Hello:

    def GET(self, name):
        return "Hello %s!" %name
