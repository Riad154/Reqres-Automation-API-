import json
import jsonpath
import unittest
import requests


class TestAPI_post_user(unittest.TestCase):

    payload = {
        "name": "morpheus",
        "job": "leader"
    }


    def test_post_user_post(self):
        self.url = "https://reqres.in/api/users"
        resp = requests.post(self.url, json=self.payload)
        self.assertEqual(resp.status_code, 201)
        print(resp.content)
        print("Test post_user Completed")




if __name__ == " __main__":
    tester = TestAPI_post_user()

    tester.test_post_user_post()

