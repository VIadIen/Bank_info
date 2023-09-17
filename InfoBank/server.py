import re
from urllib.parse import unquote
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import csv

FILE_PATH = 'database/binlist-data.csv'
DIVIDER = ','
PATTERN = r'/\d{5,12}'


# Get a database of banks and json keys
def get_bank_database():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        row = csv.DictReader(f)
        bank_database = []
        for i in row:
            bank_database += [i]
        return bank_database


# Get answer
def get_answer(card_bin, bank_database):
    card_bin = unquote(card_bin).replace(' ', '')
    try:
        card_bin = re.search(PATTERN, card_bin).group(0)[1:]
        bank = list(filter(lambda x: x['bin'] == card_bin[:8], bank_database)) or \
               list(filter(lambda x: x['bin'] == card_bin[:6], bank_database)) or \
               list(filter(lambda x: x['bin'] == card_bin[:5], bank_database))  # list of bank info
        bank_info = dict(*bank)  # answer on request
        if bank_info:
            bank_info['bank_url'] = re.sub(r"https?://", '', bank_info['bank_url'])  # url preparation
            bank_info1 = bank_info.copy()
            for key, value in bank_info1.items():  # deletion empty fields
                if not bank_info[key]:
                    del bank_info[key]
            return json.dumps(bank_info).encode('utf-8')
        else:
            raise AttributeError
    except AttributeError:
        raise AttributeError


class MyServ(BaseHTTPRequestHandler):
    def _set_response(self, code=200):
        self.send_response(code)
        self.end_headers()

    @staticmethod
    def create_page(path):
        with open(f'{path[1:]}', 'rb') as f:
            return f.read()

    def do_GET(self):
        time.sleep(2)
        if self.path == '/':
            self.path = '/index.html'
            file_to_open = self.create_page(self.path)
            self._set_response()
        elif 'generate_answer' in self.path:
            try:
                file_to_open = get_answer(self.path, database)
                self._set_response()
            except AttributeError:
                self.path = '/error.html'
                file_to_open = self.create_page(self.path)
                self._set_response(404)
        else:
            try:
                file_to_open = self.create_page(self.path)
                self._set_response()
            except OSError:
                self.path = '/error.html'
                file_to_open = self.create_page(self.path)
                self._set_response(404)
        self.wfile.write(file_to_open)


if __name__ == '__main__':
    print("I'm start")
    database = get_bank_database()
    print("I'm get database")
    server_addr = ('0.0.0.0', 4005)
    httpd = HTTPServer(server_addr, MyServ)
    print("I'm create server, try connect!")
    while True:
        try:
            print('Start server')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('Stop server')
            httpd.server_close()
            break
