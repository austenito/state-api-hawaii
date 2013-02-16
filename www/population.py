#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template

app = Blueprint('population', __name__, url_prefix='/population')


@app.route('/', methods=['GET'])
def population():
    return render_template('population.html')

# vim: filetype=python
