# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response,request
from sqlalchemy.sql import exists
from models import Article, Category, Tag, Status, Secret
from App import db, uid
from . import blog
from sqlalchemy import and_, func
from App.basefunc import get_counts_lid, json_mysql


@blog.route('/blog', methods=['GET'])
def get_blog():
    timestamp = request.args.get('timestamp')
    path = request.args.get('path')
    uarg = request.args.get('arg')
    articles = db.session.query(Article).filter(Article.category_id == 8).limit(5).all()
    categorys = db.session.query(Category).filter(Category.info == 'python').all()
    artconuts = db.session.query(func.count('*')).filter(
        Article.category_id == 8).scalar()
    if not uarg:
        if timestamp and path:  # 请求不是python页
            counts, lid = get_counts_lid(timestamp,request)
            if counts and lid:
                art = json_mysql(lid, 8)
                return jsonify({'msg': 'success', 'art': art})
            else:
                return render_template('error.html')

        else:  # 请求是初始python页
            articles_1 = articles[:25]
            return render_template('blog.html', cat=categorys, art=articles_1, counts=artconuts)

    return render_template('blog.html', art=articles, cat=categorys, counts=artconuts)
