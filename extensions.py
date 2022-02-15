import requests
import json

from Config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):

        if quote == base:
            raise ConvertionException(f'Вы ввели одинаковые волюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удолось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удолось обработать валюту {base}')
        try:
            amount = int(amount)
        except ValueError:
            raise ConvertionException(f'Не удолось обработать клоличество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * int(amount)

        return total_base
