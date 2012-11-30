# -*- coding: utf-8 -*-

# author: notedit <notedit@gmail.com>
# date: 2012/12/01  morning

import sys 
import time
import flask
from flask import Blueprint
from flask import request
from flask import g
from flask import Response
from flask import current_app
from flask import session
from flask import jsonify
from flask.views import MethodView
from flask.views import View


instance = Blueprint('index',__name__)

class TestView(MethodView):
    def get(self):
        return jsonify(hello="""do not panic""")

instance.add_url_rule('/test',view_func=TestView.as_view('test'),methods=['GET',])
