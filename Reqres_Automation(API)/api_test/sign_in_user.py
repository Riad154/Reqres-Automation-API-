import json
import jsonpath
import unittest
import requests



class TestAPI(unittest.TestCase):
    # API url
    url = "https://reqres.in/api/login"

    test_1_payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    test_3_payload = {
        "email": "sydney@fife"
    }



    def test_1_post(self):
        resp = requests.post(self.url, json=self.test_1_payload)
        self.assertEqual(resp.status_code, 200)
        print(resp.content)
        print("Test 1 Completed")


    def test_2_post(self):
        self.test_2_url = "https://api-dev.knightsbridge.live/api/users/signin"
        resp = requests.get(self.test_2_url)
        code = resp.status_code
        assert code == 404
        print(resp.content)
        print("Test 2 Completed")

    def test_3_post(self):
        self.test_3_url = "https://reqres.in/api/login"
        resp = requests.get(self.test_3_url)
        code = resp.status_code
        assert code == 200
        print(resp.content)
        print("Test 3 Completed")





if __name__ == " __main__":
    tester = TestAPI()

    tester.test_1_post()
    tester.test_2_post()
    tester.test_3_post()




