#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

app = Blueprint('population', __name__, url_prefix='/population')


@app.route('/', methods=['GET'])
def population():

# vim: filetype=python
