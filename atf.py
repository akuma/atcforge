#coding=utf-8

""" Basic todo list using webpy 0.3 """

import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete'
)


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull, description='控制文件名称'),
        web.form.Textbox('encoding', web.form.notnull, description='文件编码'),
        web.form.Textbox('is_enable', web.form.notnull, description='是否启用'),
        web.form.Textbox('description', web.form.notnull, description='描述信息'),
        web.form.Button('Add control file'),
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



class Delete:

    def POST(self, id):
        """ Delete based on ID """
        model.del_control(id)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
