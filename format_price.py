import sys
from decimal import Decimal, InvalidOperation


def convert_to_decimal(price):
    try:
        return Decimal(price).quantize(Decimal('.00'))
    except InvalidOperation as err:
        return


def format_price(price):
    price_decimal = convert_to_decimal(price)
    if price_decimal:
        return '{:,}'.format(price_decimal.normalize()).replace(',', ' ')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        price = convert_to_decimal(sys.argv[1])
        if price:
            print(price)
        else:
            print("Incorrect value")
