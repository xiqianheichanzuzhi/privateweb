# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response,request
from sqlalchemy.sql import exists
from models import Article, Category, Tag, Status, Secret
from App import db, uid
from sqlalchemy import and_, func
from App.basefunc import get_counts_lid, json_mysql
from . import news



@news.route('/news', methods=['GET'])
def news():
    categorys = db.session.query(Category).filter(Category.info == 'python').all()
    articles = db.session.query(Article).filter(Article.category_id==7).limit(10).all()

    return render_template('news.html',cat=categorys,art=articles)