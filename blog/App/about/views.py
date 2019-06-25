# -*- coding:utf-8 -*-
from flask import render_template, url_for, redirect, request, jsonify, session, g, make_response

from . import about



@about.route('/about', methods=['GET'])
def about():
    return render_template('about.html')