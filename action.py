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
def new_form(is_modify=False, product_id=None, action_id=None):
    product_vals = []
    products = product_model.get_products()
    for p in products:
        val = (p.id, p.cname + ' (' + p.ename + ')')
        product_vals.append(val)

    # 验证 Action 编号是否已经存在
    serial_check = web.form.Validator('编号已经存在', lambda i: not action_model.serial_exists(i.product_id, i.serial, action_id));

    # 通用的字段
    serial_fld = web.form.Textbox('serial', web.form.notnull, web.form.regexp('\d+', '组件编号必须为数字'), description='组件编号')
    name_fld = web.form.Textbox('name', web.form.notnull, description='组件名称')
    state_fld = web.form.Dropdown('state', [('1', '正常'), ('0', '废弃')], web.form.notnull, description='组件状态')
    desc_fld = web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息')
    button_fld = web.form.Button(' 保存 ', class_='colorButton')

    if is_modify:
        # 设置修改页面的表单字段
        form = web.form.Form(
            web.form.Dropdown('product_id', product_vals, web.form.notnull, description='所属产品', disabled='disabled'),
            web.form.Hidden('product_id', value=product_id, description='所属产品'),
            serial_fld,
            name_fld,
            state_fld,
            desc_fld,
            button_fld,
            validators=[serial_check]
        )
    else:
        # 设置新增页面的表单字段
        form = web.form.Form(
            web.form.Dropdown('product_id', product_vals, web.form.notnull, description='所属产品'),
            serial_fld,
            name_fld,
            state_fld,
            desc_fld,
            button_fld,
            validators=[serial_check]
        )

    return form

class Index:

    def GET(self, product_id=None):
        products = list(product_model.get_products())

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
        form = new_form(True, action.product_id, id)
        form.fill(action)
        return render.action.actionEdit(id, form)

    def POST(self, id):
        form = new_form(True, action_id=id)

        if not form.validates():
            return render.action.actionEdit(id, form)

        action_model.update_action(id, form.d.serial, form.d.name, form.d.state, form.d.description)
        raise web.seeother('/p/' + form.d.product_id)

app = web.application(urls, globals())
