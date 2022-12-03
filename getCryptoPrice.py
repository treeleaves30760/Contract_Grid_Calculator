import requests
import json


class binance:
    def __init__(self) -> None:
        self.url = "https://api.binance.com"
        self.backup_url = "https://api3.binance.com"

    def get_crypto_price(self, symbol="ETHBUSD", symbols=[]):
        '''If symbols is empty, then use symbol'''
        if len(symbols):
            pass
        else:
            datas = {
                'symbol': symbol
            }
            res = requests.get(self.url + "/api/v3/ticker/price", params=datas)
            reData = json.loads(res.content.decode())
            print(reData['price'])
