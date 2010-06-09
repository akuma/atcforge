#coding=utf-8

import web
import product_model
import action_model
import control_model
from template import render

urls = (
    '/?', 'Index',
    '/new', 'New',
    '/action/(.+)', 'ActionList',
    '/del/(.+)', 'Delete',
    '/(.+)', 'Edit'
)

def new_form():
    product_vals = []
    products = product_model.get_products()
    for p in products:
        val = (p.id, p.cname + ' (' + p.ename + ')')
        product_vals.append(val)

    form = web.form.Form(
        web.form.Dropdown('product_id', product_vals, web.form.notnull, description='所属产品'),
        web.form.Textbox('name', web.form.notnull, description='文件名称'),
        web.form.Dropdown('is_enable', [('1', '启用'), ('0', '停用')], web.form.notnull, description='是否启用'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton'),
    )
    return form

class Index:

    def GET(self):
        controls = control_model.get_controls()
        return render.control.controlList(controls)

class ActionList:

    def GET(self, control_id):
        actions = action_model.get_action_of_control(control_id)
        return render.control.action_list(control_id, actions)

class New:

    """
    product_vals = []
    products = product_model.get_products()
    for p in products:
        val = (p.id, p.cname + ' (' + p.ename + ')')
        product_vals.append(val)

    form = web.form.Form(
        web.form.Dropdown('product_id', product_vals, web.form.notnull, description='所属产品'),
        web.form.Textbox('name', web.form.notnull, description='文件名称'),
        web.form.Dropdown('is_enable', [('1', '启用'), ('0', '停用')], web.form.notnull, description='是否启用'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton'),
    )
    """

    def GET(self):
        form = new_form()
        return render.control.controlNew(form)

    def POST(self):
        form = new_form()

        if not form.validates():
            return render.control.controlNew(form)

        control_model.new_control(form.d.product_id, form.d.name, form.d.is_enable, form.d.description)
        raise web.seeother('/')

class Edit:

    def GET(self, id):
        control = control_model.get_control(id)
        form = new_form()
        form.fill(control)
        return render.control.controlEdit(form)

    def POST(self, id):
        form = new_form()

        if not form.validates():
            return render.control.controlEdit(form)

        control_model.update_control(id, form.d.name, form.d.is_enable, form.d.description)
        raise web.seeother('/')

class Delete:

    def GET(self, id):
        control_model.del_control(id)
        raise web.seeother('/')

app = web.application(urls, globals())
