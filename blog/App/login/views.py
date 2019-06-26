# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response
from sqlalchemy.sql import exists
from models import User
from random import randint
from App import db, uid
from . import login
import arrow


@login.route('/register', methods=['GET', 'POST'])
def get_register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        regmap = {
            'u': '用户名',
            'e': '邮箱',
            't': '手机',
        }
        user_name = json.loads(request.form.get('data')).get('u')
        flag = json.loads(request.form.get('data')).get('i')
        flag_value = regmap.get(flag)
        user_exsits = db.session.query(exists().where(User.user_name == user_name)).scalar()
        info = '{0}已存在' if user_exsits else '{0}可注册'
        db.session.close()
        return jsonify({'msg': info.format(flag_value)})


@login.route('/reg', methods=['POST'])
def get_reg():
    suc = json.loads(request.form.get('data')).get('success')
    if suc:
        info = json.loads(request.form.get('data')).get('info')
        # 头像初始化的时候随机选择
        head_pos = './static/iamges/headimg/{0}.jpg'.format(randint(0, 5))
        # 返回账号注册成功
        print(info, '================')
        # 随机昵称
        pickName = uid.RandomPickName(str(info[0]))
        db.session.add_all([User(str(info[0]), str(info[1]), pickName, head_pos, int(info[4]), info[3], 1,
                                 arrow.now().format('YYYY-MM-DD HH:MM:SS'))])
        db.session.commit()
        # 加密返回跳转连接
        p = re.compile(r"(\w)(\1+)")
        x = p.findall((info[0] + info[3]).replace('.', '').replace('@', ''))
        x = ''.join([i[0] for i in x])
        s = codecs.encode(x, "rot13")
        m = make_response(jsonify(msg='success', relname='pickname', uid=s))
        m.set_cookie('u', s)
        session['uid'] = s
        session['u'] = info[0]
        return m


@login.route('/pickname', methods=['GET', 'POST'])
def get_pickname():
    uid = session.get('uid')
    uname = session.get('u')
    if request.method == 'GET':
        u = request.args.get('uid')
        if uid and uid == u:
            m = make_response(render_template('pickname.html', status='注册成功'))
            return m
        else:
            return render_template('pickname.html', status='注册异常')
    elif request.method == 'POST':
        d = request.form.to_dict()
        u = d.get('u')
        if uid and uid == u:
            pickname = d.get('pickname')
            sex = (True if d.get('sex') == '1' else False)
            info = db.session.query(User).filter_by(user_name=uname).first()
            if info:
                if pickname == '':
                    info.user_sex = sex
                    db.session.commit()
                # 入库，修改昵称和性别
                else:
                    info.user_nickname = str(pickname)
                    info.user_sex = sex
                    db.session.commit()
                return jsonify({'msg': '1', 'path': 'index', 'p': str(pickname)})
            else:
                return render_template('pickname.html', status='注册异常')
        else:
            return render_template('pickname.html', status='注册异常')


# 登陆验证
@login.route('/login', methods=['POST'])
def get_login():
    suc = request.form.to_dict()
    u, p = suc.get('u'), suc.get('p')
    info = db.session.query(User).filter_by(user_name=u).first()
    if info:
        if p == info.user_password:
            return jsonify({'msg': '1', 'path': 'index', 'p': str(info.user_nickname)})
        else:
            return jsonify({'msg': '0', 'path': 'registerp'})  # 密码错误
    else:
        return jsonify({'msg': '0', 'path': 'registeru'})  # 账号错误
