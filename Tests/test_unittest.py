import requests
import unittest

URL = 'http://localhost:4000/generate_answer'


class Test(unittest.TestCase):
    def test_connection(self):
        self.assertEqual(str(requests.get('http://localhost:4000/')), '<Response [200]>', 'Connection failed')

    def test_get_correct_ans_default(self):
        self.assertEqual(requests.get(f'{URL}/201423').json(),
                         {'bin': '201423', 'brand': 'ENROUTE', 'type': 'CREDIT', 'issuer': 'AIR CANADA',
                          'alpha_2': 'CA', 'alpha_3': 'CAN', 'country': 'Canada', 'latitude': '56.1304',
                          'longitude': '-106.347', 'bank_phone': '1-800-234-6377',
                          'bank_url': 'www.dinersclub.com/'},
                         'Incorrect answer')

    def test_get_incorrect_ans_digit(self):
        self.assertEqual(str(requests.get(f'{URL}/00000000')), '<Response [404]>', 'Incorrect code')

    def test_get_incorrect_ans_alpha(self):
        self.assertEqual(str(requests.get(f'{URL}/abcde')), '<Response [404]>', 'Incorrect code')

    def test_get_correct_ans_small(self):
        self.assertEqual(requests.get(f"{URL}/503989").json(), {"bin": "503989", "brand": "MAESTRO", "type": "DEBIT"},
                         'Incorrect answer')

    def test_get_correct_ans_space(self):
        self.assertEqual(requests.get(f"{URL}/5039 8912 3564 1234").json(),
                         {"bin": "503989", "brand": "MAESTRO", "type": "DEBIT"},
                         'Incorrect answer')

    def test_get_incorrect_ans_mark(self):
        self.assertEqual(str(requests.get(f'{URL}/?503999')), "<Response [404]>", 'Incorrect answer')


if __name__ == '__main__':
    unittest.main()
