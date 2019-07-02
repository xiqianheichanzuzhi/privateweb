# -*- coding:utf-8 -*-
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response
from models import Article, Category, Tag, Status, Secret
from App import db
from . import mypython
from App.basefunc import get_counts_lid, json_mysql
from sqlalchemy import and_, func


@mypython.route('/mypython', methods=['GET'])
def mypython():
    timestamp = request.args.get('timestamp')
    path = request.args.get('path')
    uarg = request.args.get('arg')
    categorys = db.session.query(Category).filter(Category.info == 'python').all()
    articles = db.session.query(Article).filter(Article.category_id < 4).limit(5).all()
    artconuts = db.session.query(func.count('*')).filter(Article.category_id < 4).scalar()

    if not uarg:
        if timestamp and path:  # 请求不是python页
            counts, lid = get_counts_lid(timestamp,request)
            if counts and lid:
                art = json_mysql(lid,4)
                return jsonify({'msg': 'success', 'art': art})
            else:
                return render_template('error.html')

        else:  # 请求是初始python页
            articles_1 = articles[:25]
            return render_template('mypython.html', cat=categorys, art=articles_1, counts=artconuts)
    else:
        uarg = uarg.replace('?', '')
        for i in categorys:  # 判断传入参数是否是python分类
            if i.category_title == uarg:
                # 找到改分类的id

                cid = db.session.query(Category).filter(Category.category_title==uarg).first().id
                if timestamp and path:  # 请求点击加载

                    counts, lid = get_counts_lid(timestamp,request)
                    if counts and lid:
                        art = json_mysql(lid,cid)
                        return jsonify({'msg': 'success', 'art': art})
                    else:
                        return render_template('error.html')

                else:    # 请求是初始python页
                    articles_uarg = db.session.query(Article).filter(
                        Article.category_id == i.id).limit(1).all()
                    artconuts = db.session.query(func.count('*')).filter(
                        Article.category_id == i.id).scalar()
                    return render_template('mypython.html', cat=categorys, art=articles_uarg[:25], counts=artconuts)
        else:
            return render_template('error.html')


