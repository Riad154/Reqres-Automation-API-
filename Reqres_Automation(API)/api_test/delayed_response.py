import json
import jsonpath
import unittest
import requests


class TestAPI_delayed_response(unittest.TestCase):

    def test_delayed_response_get(self):
        self.url = "https://reqres.in/api/users?delay=3"
        self.headers = {'content-type': 'multipart/form-data'}
        resp = requests.get(self.url, headers=self.headers)
        code = resp.status_code
        assert code == 200
        print(resp.headers)
        print(resp.content)
        print("Test single_user Completed")




if __name__ == " __main__":
    tester = TestAPI_delayed_response()

    tester.test_delayed_response_get()


