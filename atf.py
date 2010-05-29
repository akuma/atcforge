#coding=utf-8

""" Autotest manager app using webpy 0.3 """

import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/control/(.+)/del', 'DeleteControl',
    '/control/(.+)', 'ViewControl',
    '/hello/(.+)', 'Hello',
)


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull, description='文件名称', class_='titleTd'),
        web.form.Dropdown('encoding', ['UTF-8', 'GBK'], web.form.notnull, description='文件编码'),
        web.form.Dropdown('is_enable', ['YES', 'NO'], web.form.notnull, description='是否启用'),
        web.form.Textarea('description', web.form.notnull,
            rows=10, cols=80, description='描述信息'),
        web.form.Button(' 保存 ', class_='colorButton'),
    )

    def GET(self):
        """ Show page """
        controls = model.get_controls()
        form = self.form()
        return render.index(controls, form)

    def POST(self):
        """ Add new control file """
        form = self.form()

        if not form.validates():
            controls = model.get_controls()
            return render.index(controls, form)

        model.new_control(form.d.name, form.d.encoding, form.d.is_enable, form.d.description)
        raise web.seeother('/')

class ViewControl:

    def GET(self, id):
        """ Select based on ID """
        control = model.get_control(id)
        form = Index.form()
        form.fill(control)
        controls = model.get_controls()
        return render.index(controls, form)

    def POST(self, id):
        form = Index.form()
        """control = model.get_control(id)"""

        if not form.validates():
            """form.fill(control)"""
            controls = model.get_controls()
            return render.index(controls, form)

        model.update_control(id, form.d.name, form.d.encoding, form.d.is_enable, form.d.description)
        raise web.seeother('/')

class DeleteControl:

    def GET(self, id):
        model.del_control(id)
        raise web.seeother('/')

class Hello:

    def GET(self, name):
        return "Hello %s!" %name

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
