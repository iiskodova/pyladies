import qrcode
import requests
import json
from datetime import datetime

SOURCE_FILE = 'rates.json'
KURZY_API = "https://data.kurzy.cz/json/meny/b[6].json"
TEMPLATE = 'template.txt'
ACCOUNT = 'CZ5562106701002204758351'

class Invoice:

    def download(self, url=KURZY_API, file=SOURCE_FILE):
        r = requests.get(url)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(r.text)

    def get_data(self, filename=SOURCE_FILE):
        with open(filename) as f:
            self.rates = json.loads(f.read())

    def currency_exchange(self, amount, currency):
        czk = ['KC', 'KČ', 'CZK']

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f'Chybná hodnota, prosím zadej znovu částku: {amount}')

        if amount < 0:
            raise ValueError(f'Chybná hodnota, prosím zadej znovu částku: {amount}')

        if currency in czk:
            self.final_amount = str(amount)
        elif currency in self.rates['kurzy']:
            amount = amount * self.rates['kurzy'][currency]['dev_stred']
            self.final_amount = str(amount)
        else:
            raise CurrencyError(f'Chybně zadabná měna: {currency}')

    def v_symbol(self):
        self.symbol = datetime.now()
        return self.symbol

    def generate_qr_code(self):
        img = qrcode.make(f'SPD*1.0*ACC:{ACCOUNT}*AM:{self.result}*CC:CZK*MSG:{message}*X-VS:{v_symbol}')
        img_qr = 'invoice' + v_symbol() + '.png'
        img.save(img_qr)

    def create_invoice(self):
        with open(file, 'r', encoding='utf-8') as f:
            template = (f.read())
            template = template.replace('SYMBOL', self.symbol)
            template = template.replace('AMOUNT', self.final_amount)
            template = template.replace('POZNAMKA', poznamka)
            template = template.replace('ACCOUNT', ACCOUNT)
            template = template.replace('QRCODE', img_qr)

        new_file = 'invoice' + self.symbol + '.html'

        with open(new_file, 'w', encoding='utf-8') as file:
            file.write(template)

class CurrencyError(Exception):
    pass


if __name__ == '__main__':
    faktura = Invoice()
    amount = input('Částka: ')
    currency = input('Měna: ').upper()
    poznamka = input('Poznámka pro příjemce: ')
    faktura.currency_exchange(amount, currency)
    faktura.v_symbol()
    faktura.create_invoice(poznamka)
