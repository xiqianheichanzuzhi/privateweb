# -*- coding:utf-8 -*-
import os
from flask_session import Session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from modelview import BaseModelview, UserAdmin, MessageAdmin,Secretadmin
from flask_ckeditor import CKEditor  # 导入扩展类 CKEditor 和 字段类 CKEditorField

db = SQLAlchemy()


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(BASE_DIR, r'App\templates')
    static_dir = os.path.join(BASE_DIR, r'App\static')

    app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)  # 引入app实例
    ''':exception 蓝图注册部分'''
    app.config.from_object('config')
    from App.login import views, login
    app.register_blueprint(blueprint=login)  # 将app交由blue管理   登陆
    from App.life import views, life
    app.register_blueprint(blueprint=life)  # 将app交由blue管理    首页
    from App.blog import views, blog
    app.register_blueprint(blueprint=blog)  # 将app交由blue管理    blog
    from App.about import views,about
    app.register_blueprint(blueprint=about)  # 将app交由blue管理    关于我
    from App.sercet import views,sercet
    app.register_blueprint(blueprint=sercet)  # 将app交由blue管理    福利
    from App.mypython import views,mypython
    app.register_blueprint(blueprint=mypython)  # 将app交由blue管理    python
    from App.news import views,news
    app.register_blueprint(blueprint=news)  # 将app交由blue管理    新闻
    ''':exception flask_admin部分'''
    admin = Admin(app, name='web', template_mode='bootstrap3')
    db.init_app(app)
    ''':exception 数据库扩展部分'''
    from models import AdminUser, Tag, Article,Status,Category,Secret
    ckeditor = CKEditor()
    ckeditor.init_app(app)
    admin.add_view(UserAdmin(AdminUser, db.session, name=u'用户管理'))
    admin.add_view(BaseModelview(Status, db.session, name=u'状态管理'))
    admin.add_view(BaseModelview(Tag, db.session, name=u'标签管理'))
    admin.add_view(BaseModelview(Category, db.session, name=u'分类管理'))
    admin.add_view(MessageAdmin(Article, db.session, name=u'文章管理'))
    admin.add_view(Secretadmin(Secret,db.session,name = u'福利内容'))
    ''':exception flask国际化'''
    from flask_babelex import Babel
    babel = Babel(app)
    ''':exception Session部分'''
    Session(app)
    return app
