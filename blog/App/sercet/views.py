# -*- coding:utf-8 -*-
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response

from . import sercet



@sercet.route('/sercet', methods=['GET'])
def blog():
    return render_template('sercet.html')
