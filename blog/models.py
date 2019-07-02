# encoding:utf-8
# 定义1个类(由db.Model继承)，注意这个类是数据库真实存在的，因为我是针对已有数据库做转化
# 我的数据库结构见下图 其中role是数据库的一张表名
from App import db, create_app
from datetime import datetime
import os.path as op

file_path = op.join(op.dirname(__file__), 'static')  # 文件上传路径


class User(db.Model):
    __tablename__ = "blog_users"

    # id是主键db.Column是字段名， db.INT是数据类型
    user_id = db.Column(db.INT, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), unique=True)
    user_password = db.Column(db.String(10), unique=False)
    user_nickname = db.Column(db.String(40), unique=True, default=None)
    user_headimg = db.Column(db.String(99), unique=False, default=None)
    user_tel = db.Column(db.String(11), unique=False, default=None)
    user_email = db.Column(db.String(99), unique=True)
    user_sex = db.Column(db.Boolean, default=1)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)

    c = db.relationship('Comment', backref='user', lazy='dynamic')
    # r = db.relationship('Article', backref='user', lazy='dynamic')
    # s = db.relationship('Status', backref='user', lazy='dynamic')

    def __init__(self, user_name, user_password, user_nickname, user_headimg, user_tel, user_email, user_sex,
                 create_time):
        self.user_name = user_name
        self.user_password = user_password
        self.user_nickname = user_nickname
        self.user_headimg = user_headimg
        self.user_tel = user_tel
        self.user_email = user_email
        self.user_sex = user_sex
        self.create_time = create_time


class Comment(db.Model):
    __tablename__ = "blog_comments"

    comments_id = db.Column(db.INT, primary_key=True, autoincrement=True)
    comments_contents = db.Column(db.String(300), unique=False)
    comments_posttime = db.Column(db.DateTime)
    parents_id = db.Column(db.String(300))
    comments_level = db.Column(db.INT)
    user_id = db.Column(db.INTEGER, db.ForeignKey('blog_users.user_id'))  # 关联用户userID
    articls_id = db.Column(db.INTEGER, db.ForeignKey('articls.articls_id'))  # 关联用户userID

    def __repr__(self):
        return '<User %r>' % self.user_id

    def __init__(self, comments_id, comments_contents, comments_posttime, parents_id, comments_level, user_id,
                 articls_id):
        self.comments_id = comments_id
        self.comments_contents = comments_contents
        self.comments_posttime = comments_posttime
        self.parents_id = parents_id
        self.comments_level = comments_level
        self.user_id = user_id
        self.articls_id = articls_id


class Status(db.Model):
    __tablename__ = "status"

    status_id = db.Column(db.INT, primary_key=True, autoincrement=True)
    status_title = db.Column(db.String(300), unique=False)
    status_contents = db.Column(db.String(3000), unique=False)
    status_posttime = db.Column(db.DateTime)
    # Article = db.relationship('Article', backref='Article', lazy='dynamic')

class AdminUser(db.Model):
    __tablename__ = "admin_user"

    # id是主键db.Column是字段名， db.INT是数据类型
    user_id = db.Column(db.INT, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), unique=True)
    user_password = db.Column(db.String(10), unique=False)
    user_nickname = db.Column(db.String(40), unique=True, default=None)
    user_headimg = db.Column(db.String(99), unique=False, default=None)
    user_tel = db.Column(db.INT, unique=False, default=None)
    user_email = db.Column(db.String(99), unique=True)
    user_sex = db.Column(db.Boolean, default=1)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)

    # c = db.relationship('Comment', backref='user', lazy='dynamic')
    # r = db.relationship('Article', backref='user', lazy='dynamic')
    # s = db.relationship('Status', backref='user', lazy='dynamic')


class Article(db.Model):
    __tablename__ = "articls"

    articls_id = db.Column(db.INT, primary_key=True, autoincrement=True)
    articls_title = db.Column(db.String(300), unique=False)
    articls_desc = db.Column(db.String(64), nullable=True)
    articls_contents = db.Column(db.Text, unique=False)
    articls_posttime = db.Column(db.DateTime)
    articls_category = db.Column(db.String(99), unique=False, default=None)
    articls_headimg = db.Column(db.String(99), unique=False, default=None)
    # user_id = db.Column(db.INTEGER, db.ForeignKey('admin_user.user_id'))  # 关联用户userID
    tag_id = db.Column(db.INTEGER, db.ForeignKey('tag.id'))  # 关联标签ID
    category_id =  db.Column(db.INTEGER, db.ForeignKey('category.id'))  # 关联分类ID
    comment = db.relationship('Comment', backref='comment', lazy='dynamic')
    tag = db.relationship('Tag', backref='tag')
    category = db.relationship('Category', backref='status')

class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    desc = db.Column(db.String(64), nullable=True)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)
    Article = db.relationship('Article',  lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.name

class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_title= db.Column(db.String(300), unique=False)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)
    Article = db.relationship('Article',  lazy='dynamic')
    info = db.Column(db.String(255), unique=False)
    # Article = db.relationship('Article', backref='Article', lazy='dynamic')

class Secret(db.Model):
    __tablename__ = "Secret"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    secret_title= db.Column(db.String(300), unique=False)
    secret_desc = db.Column(db.String(64), nullable=True)
    secret_content= db.Column(db.String(300), unique=False)
    secret_img = db.Column(db.String(9999), unique=False, default=None)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)


class News(db.Model):
    __tablename__ = "News"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    news_cate = db.Column(db.String(300), unique=False)
    news_title= db.Column(db.String(300), unique=False)
    news_desc = db.Column(db.String(64), nullable=True)
    news_content= db.Column(db.String(9999), unique=False)
    news_img = db.Column(db.String(9999), unique=False, default=None)
    news_imgcounts = db.Column(db.Integer, unique=False, default=None)
    news_paltform  = db.Column(db.String(64), nullable=True)
    news_author =  db.Column(db.String(64), nullable=True)
    news_readcounts = db.Column(db.String(64), nullable=True)
    crawled_time = db.Column(db.DateTime, nullable=True, default=datetime.now)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)
    def __repr__(self):
        return '<User %r>' % self.id

    def __init__(self, id, news_cate,news_title, news_desc, news_content,news_img, news_imgcounts, news_paltform,
                 news_author,crawled_time,create_time):
        self.news_cate = news_cate
        self.news_title = news_title
        self.news_desc = news_desc
        self.news_content = news_content
        self.news_img = news_img
        self.news_imgcounts = news_imgcounts
        self.news_paltform = news_paltform
        self.news_author = news_author
        self.crawled_time = crawled_time
        self.create_time = create_time


db.create_all(app=create_app())

# 初始化role 并插入数据库
# db.create_all()
# test_role1 = Role(1 ,'supervisol', '超超超超级管理员哦')
#
# test_role2 = Role(2,'your try', '你试试哦')
# db.session.add_all([test_role1,test_role2])
# db.session.commit()


# #查询数据库
# a = db.session.query(Role).filter_by(id=2).first()  # 查询role表中id为2的第一个匹配项目，用".字段名"获取字段值
# print(a)
# db.session.query(role).all()  # 得到一个list，返回role表里的所有role实例
# db.session.query(role).filter(role.id == 2).first() # 结果与第一种一致
# # 获取指定字段，返回一个生成器 通过遍历来完成相关操作, 也可以强转为list
# db.session.query(role).filter_by(id=2).values('id', 'name', 'name_cn')
# # 模糊查询
# db.session.query(role).filter(role.name_cn.endswith('管理员')).all()  # 获取role表中name_cn字段以管理员结尾的所有内容
# # 修改数据库内容
# user = db.session.query(role).filter_by(id=6).first()  # 将role表中id为6的name改为change
# user.name = 'change'
# db.session.commit()
