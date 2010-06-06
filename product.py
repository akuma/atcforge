#coding=utf-8

import web
import product_model
from template import render

urls = (
    '/?', 'Index',
    '/new', 'New',
    '/(.+)', 'Edit'
)

class Index:

    def GET(self):
        products = product_model.get_products()
        return render.product.productList(products)

class New:

    form = web.form.Form(
        web.form.Textbox('ename', web.form.notnull, description='产品标识', class_='titleTd'),
        web.form.Textbox('cname', web.form.notnull, description='产品名称', class_='titleTd'),
        web.form.Textarea('description', web.form.notnull, rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton'),
    )

    def GET(self):
        form = self.form()
        return render.product.productNew(form)

    def POST(self):
        form = self.form()

        if not form.validates():
            return render.product.productNew(form)

        product_model.new_product(form.d.ename, form.d.cname, form.d.description)
        raise web.seeother('/')

class Edit:

    def GET(self, id):
        product = product_model.get_product(id)
        form = New.form()
        form.fill(product)
        return render.product.productEdit(form)

    def POST(self, id):
        form = New.form()

        if not form.validates():
            return render.productEdit(form)

        product_model.update_product(id, form.d.ename, form.d.cname, form.d.description)
        raise web.seeother('/')

app = web.application(urls, globals())
