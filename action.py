#coding=utf-8

import web
import product_model
import action_model
from template import render

urls = (
    '/?', 'Index',
    '/p/(.+)', 'Index',
    '/new', 'New',
    '/(.+)', 'Edit',
)

# Create a new form.
def new_form(is_modify=False, product_id=None):
    product_vals = []
    products = product_model.get_products()
    for p in products:
        val = (p.id, p.cname + ' (' + p.ename + ')')
        product_vals.append(val)

    if is_modify:
        form = web.form.Form(
            web.form.Dropdown('product_id', product_vals, web.form.notnull, description='所属产品', disabled='disabled'),
            web.form.Hidden('product_id', value=product_id, description='所属产品'),
            web.form.Textbox('serial', web.form.notnull, description='编号', class_='titleTd', ),
            web.form.Textbox('name', web.form.notnull, description='名称', class_='titleTd'),
            web.form.Dropdown('state', [('1', '正常'), ('0', '废弃')], web.form.notnull, description='状态'),
            web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
            web.form.Button(' 保存 ', class_='colorButton')
        )
    else:
        #serial_check = web.form.Validator('Action 编号已经存在', lambda x: action_model.serial_exists(x.product_id, x.serial))
        serial_check = web.form.Validator('Action 编号已经存在', lambda x: x.serial < 3)
        form = web.form.Form(
            web.form.Dropdown('product_id', product_vals, web.form.notnull, description='所属产品'),
            web.form.Textbox('serial', web.form.notnull, description='编号', class_='titleTd', validator=serial_check),
            web.form.Textbox('name', web.form.notnull, description='名称', class_='titleTd'),
            web.form.Dropdown('state', [('1', '正常'), ('0', '废弃')], web.form.notnull, description='状态'),
            web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
            web.form.Button(' 保存 ', class_='colorButton'),
            #validators = [serial_check]
        )

    return form

class Index:

    def GET(self, product_id=None):
        products = product_model.get_products()

        if products:
            if not product_id:
                product_id = products[0].id
            actions = action_model.get_actions(product_id)
        else:
            actions = []

        return render.action.actionList(products, product_id, actions)

class New:

    def GET(self):
        form = new_form()
        return render.action.actionNew(form)

    def POST(self):
        form = new_form()

        if not form.validates():
            return render.action.actionNew(form)

        action_model.new_action(form.d.product_id, form.d.serial, form.d.name, form.d.state, form.d.description)
        raise web.seeother('/p/' + form.d.product_id)

class Edit:

    def GET(self, id):
        action = action_model.get_action(id)
        form = new_form(True, action.product_id)
        form.fill(action)
        return render.action.actionEdit(form)

    def POST(self, id):
        form = new_form(True)

        if not form.validates():
            return render.action.actionEdit(form)

        action_model.update_action(id, form.d.serial, form.d.name, form.d.state, form.d.description)
        raise web.seeother('/p/' + form.d.product_id)

app = web.application(urls, globals())
