import requests
from logging import getLogger

logger = getLogger(__name__)


class BittrexError(Exception):
    '''неизвестная ошибка при запросе api'''


class BittrexRequestError(BittrexError):
    '''ошибки при некоректной работе'''


class BittrexClient(object):
    # https://api.bittrex.com/api/v1.1/public/getticker?market=BTC-LTC"
    # | tr -d '\n'
    def __init__(self):
        self.base_url = " https://api.bittrex.com/api/v1.1"

    def __request(self, method, params):
        url = self.base_url + method

        try:
            r = requests.get(url=url, params=params)
            result = r.json()
        except Exception:
            logger.exception('Bittrex error')
            raise BittrexError
        if result.get('success'):
            return result
        else:
            logger.error('Request error: %s', result.get('message'))
            raise BittrexRequestError
    """куда уходит запрос , принимает ответ , ищет ошибки , декодирует"""

    def get_ticker(self, pair):
        params = {
            "market": pair
        }
        return self.__request(method="/public/getticker", params=params)


    def get_last_price(self, pair):
        res = self.get_ticker(pair=pair)
        return res["result"]["Last"]

    """забирает нужную информацию"""
