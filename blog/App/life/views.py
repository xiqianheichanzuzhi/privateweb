# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response
from sqlalchemy.sql import exists
from models import Article, Category, Tag, Status,Secret
from random import randint
from App import db, uid
from . import life
import arrow


@life.route('/', methods=['GET'])
@life.route('/index', methods=['GET'])
def get_index():
    articles = db.session.query(Article).all()
    categorys = db.session.query(Category).filter(Category.info == 'python').all()
    tags = db.session.query(Tag).all()
    status = db.session.query(Status).all()
    secret = db.session.query(Secret).all()
    return render_template('index.html', art=articles, cat=categorys, tag=tags, sta=status,sec=secret)
