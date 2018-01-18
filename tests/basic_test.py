import unittest
import app.models.User
import requests

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        r = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(r.status_code,200)


    # def test_user_endpoint(self):
    #     r = requests.get('http://127.0.0.1:5000/')
    #     self.assertEqual(r.status_code,200)
    #     json_dict = r.json()
    #     self.assertEqual(json_dict['Status'],'Success')
    #     self.assertIsNotNone(json_dict["Data"])
