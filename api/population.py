#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

app = Blueprint('population', __name__, url_prefix='/population')


@app.route('/<regex("[0-9]{4}"):year>/<county>', methods=['GET'])
def get_population_by_year_and_county(year, county):
    return jsonify({"year": year, "county": county})

# vim: filetype=python
