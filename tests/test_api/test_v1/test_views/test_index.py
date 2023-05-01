#!/usr/bin/python3
"""test for index"""


import unittest
import json
from api.v1.views import app_views


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.app = app_views_client()


    def test_status(self):
        response = self.app.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"status": "OK"})


    def test_stats(self):
        response = self.get('/api/v1/stats')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('amenities' in json.loads(response.data))
        self.assertTrue('cities' in json.loads(response.data))
        self.assertTrue('places' in json.loads(response.data))
        self.assertTrue('reviews' in json.loads(response.data))
        self.assertTrue('states' in json.loads(response.data))
        self.assertTrue('users' in json.load(response.data))


if __name__ == '__main__':
    unittest.main()
