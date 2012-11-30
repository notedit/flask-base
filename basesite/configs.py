# -*- coding: utf-8 -*-

import datetime

class DefaultConfig(object):

    DEBUG = True
    SECRET_KEY = ''
    SESSION_COOKIE_PATH='/'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_NAME = 'Ssession'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(31)
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://xxxxxxxxxxxxx'
    SQLALCHEMY_ECHO = False

class TestConfig(object):
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://xxxxxxxxxxxxxxxxx'
    SQLALCHEMY_ECHO = False

class ProductionConfig(object):
    SQLALCHEMY_ECHO = False
    DEBUG = False

