#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

app = Blueprint('population', __name__, url_prefix='/population')


@app.route('/<year>/<county>', methods=['GET'])
def get_population_by_year_and_county(year, county):
    return jsonify({"message": "booyah"})

# vim: filetype=python
