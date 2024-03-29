# -*- coding:utf-8 -*-
import codecs, re, json, uuid
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response,request
from sqlalchemy.sql import exists
from models import Article, Category, Tag, Status, Secret
from App import db, uid
from sqlalchemy import and_, func
from App.basefunc import get_counts_lid, json_mysql
from . import sercet

@sercet.route('/sercet', methods=['GET'])
def blog():
    categorys = db.session.query(Category).filter(Category.info == 'python').all()
    secrets = db.session.query(Secret).filter().all()

    return render_template('sercet.html')
