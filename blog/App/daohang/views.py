# -*- coding:utf-8 -*-
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response

from . import daohang



@daohang.route('/daohang', methods=['GET'])
def daohang():
    return render_template('daohang.html')