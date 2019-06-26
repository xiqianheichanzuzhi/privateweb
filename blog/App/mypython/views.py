# -*- coding:utf-8 -*-
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response

from . import mypython



@mypython.route('/mypython', methods=['GET'])
def mypython():
    return render_template('mypython.html')
