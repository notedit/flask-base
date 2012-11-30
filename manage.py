# -*- coding: utf-8 -*-
# author: notedit

import os
import sys
from flask import current_app
from flask.ext.script import Manager,prompt,prompt_pass,\
        prompt_bool,prompt_choices
from flask.ext.script import Server

from basesite import create_app

manager = Manager(create_app)
app = create_app

@manager.command
def initdb():
    if prompt_bool("Are you sure? You will init your database"):
        pass

@manager.command
def dropdb():
    if prompt_bool("Are you sure? You will lose all your data!"):
        pass

@manager.option('-u','--username',dest='username',required=True)
@manager.option('-p','--password',dest='password',required=True)
@manager.option('-e','--email',dest='email',required=True)
def createuser(username=None,password=None,email=None):
    pass

manager.add_command('runserver',Server())

if __name__ == '__main__':
    manager.run()
