# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response
from sqlalchemy.sql import exists
from models import Article, Category, Tag, Status,Secret
from App import db, uid
from . import blog


@blog.route('/blog', methods=['GET'])
def get_blog():
    articles = db.session.query(Article).filter(Category.id == 8).all()
    categorys = db.session.query(Category).filter(Category.info == 'python').all()
    return render_template('blog.html', art=articles,cat=categorys)