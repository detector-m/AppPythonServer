#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :core_helper.py
@说明        :
@时间        :2020/07/23 09:42:10
@作者        :Riven
@版本        :1.0.0
'''

__author__ = 'Riven'

from collections import namedtuple

from flask import current_app, request
from flask.json import dumps

def jsonify(*args, **kwargs):
    indent = None
    separators = (',', ':')

    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] or current_app.debug:
        indent = 2
        separators = (', ', ': ')

    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1: # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs

    return current_app.response_class(dumps(data, indent=indent, separators=separators) + '\n', mimetype=current_app.config['JSONIFY_MIMETYPE']).json

