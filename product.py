#coding=utf-8

import web
import product_model
from template import render

urls = (
    '/?', 'Index',
    '/new', 'New',
    '/(.+)', 'Edit'
)

def create_form():
    form = web.form.Form(
        web.form.Textbox('ename', web.form.notnull,
                         web.form.Validator('产品标识已经存在', lambda x: not product_model.ename_exists(x)),
                         description='产品标识'),
        web.form.Textbox('cname', web.form.notnull, description='产品名称'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton')
    )
    return form

def modify_form(product_id):
    form = web.form.Form(
        web.form.Textbox('ename', web.form.notnull,
                         web.form.Validator('产品标识已经存在', lambda x: not product_model.ename_exists(x, product_id)),
                         description='产品标识'),
        web.form.Textbox('cname', web.form.notnull, description='产品名称'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton')
    )
    return form

class Index:

    def GET(self):
        products = product_model.get_products()
        return render.product.productList(products)

class New:

    def GET(self):
        form = create_form()
        return render.product.productNew(form)

    def POST(self):
        form = create_form()
        if not form.validates():
            return render.product.productNew(form)

        product_model.new_product(form.d.ename, form.d.cname, form.d.description)
        raise web.seeother('/')

class Edit:

    def GET(self, id):
        product = product_model.get_product(id)
        form = modify_form(id)
        form.fill(product)
        return render.product.productEdit(form)

    def POST(self, id):
        form = modify_form(id)
        if not form.validates():
            return render.product.productEdit(form)

        product_model.update_product(id, form.d.ename, form.d.cname, form.d.description)
        raise web.seeother('/')

app = web.application(urls, globals())
