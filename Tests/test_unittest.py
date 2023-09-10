import requests
import unittest

URL = 'http://localhost:4000'


class Test(unittest.TestCase):
    def test_connection(self):
        self.assertEqual(str(requests.get(f'{URL}')), '<Response [200]>', 'Connection failed')

    def test_get_correct_ans_default(self):
        self.assertEqual(requests.get(f'{URL}/201423').json(),
                         {'Bin': '201423', 'Brand': 'ENROUTE', 'Type': 'CREDIT', 'Issuer': 'AIR CANADA',
                          'Alpha_2': 'CA', 'Alpha_3': 'CAN', 'Country': 'Canada', 'Latitude': '56.1304',
                          'Longitude': '-106.347', 'Bank_Phone': '1-800-234-6377', 'Bank_Url': 'www.dinersclub.com/'},
                         'Incorrect answer')

    def test_get_incorrect_ans_digit(self):
        self.assertEqual(str(requests.get(f'{URL}/00000000')), '<Response [404]>', 'Incorrect answer')

    def test_get_incorrect_ans_alpha(self):
        self.assertEqual(str(requests.get(f'{URL}/abcde')), '<Response [404]>', 'Incorrect answer')

    def test_get_correct_ans_small(self):
        self.assertEqual(requests.get(f"{URL}/503989").json(), {"Bin": "503989", "Brand": "MAESTRO", "Type": "DEBIT"},
                         'Incorrect answer')

    def test_get_correct_ans_space(self):
        self.assertEqual(requests.get(f"{URL}/5039 8912 3564 1234").json(), {"Bin": "503989", "Brand": "MAESTRO", "Type": "DEBIT"},
                         'Incorrect answer')


if __name__ == '__main__':
    unittest.main()
