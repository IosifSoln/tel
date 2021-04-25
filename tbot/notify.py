
from bittrex import BittrexClient
from bittrex import BittrexError



"""функция берущая  информацию с биттрекс"""
def main(NOTIFY_PAIR):
    client = BittrexClient()
    try:
        current_price = client.get_last_price(pair=NOTIFY_PAIR)
        message = '{} = {}'.format(NOTIFY_PAIR, current_price)
    except BittrexError:
        message = 'Проиошла ошибка'
    return message

if __name__ == '__main__':
    main()
