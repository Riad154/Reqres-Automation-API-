import json
import jsonpath
import unittest
import requests


class TestAPI_single_user(unittest.TestCase):


    def test_single_user_get(self):
        self.url = "https://reqres.in/api/users/2"
        self.headers = {'content-type': 'multipart/form-data'}
        resp = requests.get(self.url, headers=self.headers)
        code = resp.status_code
        assert code == 200
        print(resp.headers)
        print(resp.content)
        print("Test single_user Completed")


    def test_single_user_invalid_get(self):
        self.invalid_url = "https://reqres.in/api/users/23"
        self.headers = {'content-type': 'multipart/form-data'}
        resp = requests.get(self.invalid_url, headers=self.headers)
        code = resp.status_code
        assert code == 404
        print(resp.headers)
        print(resp.content)
        print("Test single_user_invalid Completed")







if __name__ == " __main__":
    tester = TestAPI_single_user()

    tester.test_single_user_get()
    tester.test_single_user_invalid_get()

