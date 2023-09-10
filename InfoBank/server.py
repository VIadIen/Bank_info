import re
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

FILE_PATH = 'database/binlist-data.csv'
DIVIDER = ','
PATTERN = r'/\d{5,12}'


# Get a database of banks and json keys
def get_bank_database():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        bank_info = [i.title() for i in f.readline().strip().split(DIVIDER)]  # list of attributes
        bank_database = []  # list of database
        for i in f.readlines():
            new_line = i.strip().replace(f'{DIVIDER}', f'{DIVIDER}a')
            new_line = new_line.replace(f'{DIVIDER}a ', f'{DIVIDER} ')  # for correct split using various separators
            new_line = re.sub(r"https?://", '', new_line)  # url preparation
            bank_database.extend([re.split(fr'{DIVIDER}\S', new_line)])
        return bank_info, bank_database


# Get answer
def get_answer(card_bin, bank_info, bank_database):
    card_bin = card_bin.replace('%20', '')
    try:
        card_bin = re.search(PATTERN, card_bin).group(0)[1:]
        bank = list(*filter(lambda x: x[0] == card_bin[:8], bank_database)) or \
               list(*filter(lambda x: x[0] == card_bin[:6], bank_database)) or \
               list(*filter(lambda x: x[0] == card_bin[:5], bank_database))  # list of bank info
        bank_info = dict(zip(bank_info, bank))  # answer on request
        bank_info1 = bank_info.copy()
        for key, value in bank_info1.items():  # deletion empty fields
            if not bank_info[key]:
                del bank_info[key]
        if bank_info:
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
        try:
            file_to_open = self.create_page(self.path)
            self._set_response()
        except OSError:
            try:
                file_to_open = get_answer(self.path, bank_attributes, database)
                self._set_response()
            except AttributeError:
                self.path = '/error.html'
                file_to_open = self.create_page(self.path)
                self._set_response(404)
        self.wfile.write(file_to_open)


if __name__ == '__main__':
    print("I'm start")
    bank_attributes, database = get_bank_database()
    print("I'm get database")
    server_addr = ('localhost', 4005)
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
