import json
import jsonpath
import unittest
import requests


class TestAPI_update_user(unittest.TestCase):

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    def test_update_user_post(self):
        self.url = "https://reqres.in/api/users/2"
        resp = requests.post(self.url, json=self.payload)
        self.assertEqual(resp.status_code, 201)
        print(resp.content)
        print("Test post_user_invalid Completed")




if __name__ == " __main__":
    tester = TestAPI_update_user()

    tester.test_update_user_post()

