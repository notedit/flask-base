# -*- coding: utf-8 -*-

import json
from tests import TestCase


class TestSite(TestCase):

    def test_site(self):

        resp = self.client.get('/test')
        res = json.loads(resp.data)
        assert res['hello'] == """do not panic"""




