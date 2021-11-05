import json
import jsonpath
import unittest
import requests


class TestAPI_post_user_invalid(unittest.TestCase):

    payload = {
        "email": "sydney@fife"
    }

    def test_post_user_invalid_post(self):
        self.url = "https://reqres.in/api/register"
        resp = requests.post(self.url, json=self.payload)
        self.assertEqual(resp.status_code, 400)
        print(resp.content)
        print("Test post_user_invalid Completed")




if __name__ == " __main__":
    tester = TestAPI_post_user_invalid()

    tester.test_post_user_invalid_post()

