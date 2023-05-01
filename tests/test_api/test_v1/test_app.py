#!/usr/bin/python3
"""test for app"""


import unittest
import json
from app import app


class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_status_route(self):
        response = self.app.get('/api/v1/status')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'status_code', 404})
        self.assertEqual(data, {'error': 'Not found'})


if __name__ == '__main__':
    unittest.main()
