from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask_admin import form
from flask import url_for
import os.path as op
from jinja2 import Markup
from flask_ckeditor import CKEditorField  # 导入扩展类 CKEditor 和 字段类 CKEditorField

file_path = op.join(op.dirname(__file__), 'App\static')  # 文件上传路径


class BaseModelview(ModelView):
    def getinfo(self):
        return "this is another model"


class UserAdmin(BaseModelview):
    # 设置缩略图的
    def _list_thumbnail(view, context, model, name):
        if not model.user_headimg:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.user_headimg)))

    # 格式化列表的图像显示
    column_formatters = {
        'user_headimg': _list_thumbnail
    }
    # 扩展列表显示的头像为60*60像素
    form_extra_fields = {
        'user_headimg': form.ImageUploadField('user_headimg',
                                              base_path=file_path,
                                              relative_path='images/headimgs/',
                                              thumbnail_size=(60, 60, True))
    }


# 自定义 Post 模型
# class PostArticle(ModelView):
#     form_overrides = dict(text=CKEditorField)  # 重写表单字段，将 text 字段设为 CKEditorField
#     create_template = 'edit.html'  # 指定创建记录的模板
#     edit_template = 'edit.html'  # 指定编辑记录的模板


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class MessageAdmin(BaseModelview):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']


    form_overrides = {
        'articls_contents': CKTextAreaField
    }
    # 设置缩略图的
    def _list_thumbnail(view, context, model, name):
        if not model.articls_headimg:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.articls_headimg)))

    # 格式化列表的图像显示
    column_formatters = {
        'articls_headimg': _list_thumbnail
    }


    form_extra_fields = {
        'articls_headimg': form.ImageUploadField('articls_headimg',
                                                 base_path=file_path,
                                                 relative_path='images/articleimgs/',
                                                 thumbnail_size=(215, 111, True))
    }



class Secretadmin(BaseModelview):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']


    form_overrides = {
        'secret_content': CKTextAreaField
    }
    # 设置缩略图的
    def _list_thumbnail(view, context, model, name):
        if not model.secret_img:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.secret_img)))

    # 格式化列表的图像显示
    column_formatters = {
        'secret_img': _list_thumbnail
    }


    form_extra_fields = {
        'secret_img': form.ImageUploadField('secret_img',
                                                 base_path=file_path,
                                                 relative_path='images/secretimgs/',
                                                 thumbnail_size=(215, 111, True))
    }


'''
这里有一个定义的BaseModelview是作为一个全局的Modelview来用的，
是为了自定义一些model的view界面上的显示的。里面什么都没有，
如果后期扩展权限限制了，
可以在这里加代码限制。
'''
