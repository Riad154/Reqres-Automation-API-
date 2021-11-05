import json
import jsonpath
import unittest
import requests


class TestAPI_list_users(unittest.TestCase):

    url = "https://reqres.in/api/users?page=2"

    def test_list_user_get(self):
        self.headers = {'content-type': 'multipart/form-data'}
        resp = requests.get(self.url, headers=self.headers)
        code = resp.status_code
        assert code == 200
        print(resp.content)
        print(resp.headers)
        print("Test list_user Completed")




if __name__ == " __main__":
    tester = TestAPI_list_users()

    tester.test_list_user_get()

