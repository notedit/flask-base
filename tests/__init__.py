# -*- coding: utf-8 -*-

import unittest

from basesite import create_app
from basesite import configs

class TestCase(unittest.TestCase):

    def __init__(self,*args,**kwargs):
        self.app = create_app(configs.TestConfig)
        self.app.config['TESTING'] = True
        super(TestCase,self).__init__(*args,**kwargs)

    def setUp(self):
        print '不写单元测试的人注定一辈子敲代码'
        pass

    def tearDown(self):
        print 'hello world, do not panic'
        pass
