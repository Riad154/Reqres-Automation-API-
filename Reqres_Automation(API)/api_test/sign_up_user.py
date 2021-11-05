import json
import jsonpath
import unittest
import requests


class TestAPI(unittest.TestCase):
    # API url
    url = "https://reqres.in/api/register"

    test_1_payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    test_3_payload = {
        "email": "sydney@fife"
    }



    def test_1_post(self):
        resp = requests.post(self.url, json=self.test_1_payload)
        self.assertEqual(resp.status_code, 200)
        print(resp.content)
        print("Test 1 Completed")

    def test_2_get(self):
        self.headers = {'content-type': 'multipart/form-data'}
        self.test_2_url = "https://reqres.in/api/users/23"
        resp = requests.get(self.test_2_url, headers=self.headers)
        code = resp.status_code
        assert code == 404
        print(resp.content)
        print(resp.headers)
        print("Test 2 Completed")

    def test_3_post(self):
        self.test_3_url = "https://reqres.in/api/register"
        resp = requests.post(self.test_3_url, json=self.test_3_payload)
        self.assertEqual(resp.status_code, 400)
        print(resp.content)
        print("Test 3 Completed")

    def test_4_post(self):
        self.test_4_url = "https://reqres.in/api/register"
        resp = requests.post(self.test_4_url, json=self.test_3_payload)
        self.assertEqual(resp.status_code, 400)
        print(resp.content)
        print("Test 4 Completed")


if __name__ == " __main__":
    tester = TestAPI()

    tester.test_1_post()
    tester.test_2_get()
    tester.test_3_post()
    tester.test_4_post()
