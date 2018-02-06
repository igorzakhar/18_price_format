import sys
from decimal import Decimal, InvalidOperation


def convert_to_decimal(price):
    try:
        return Decimal(price).quantize(Decimal('.00'))
    except InvalidOperation as err:
        return err


def format_price(price):
    try:
        return '{:,}'.format(price.normalize()).replace(',', ' ')
    except AttributeError as err:
        raise ValueError('Argument <price> has invalid value.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        price = convert_to_decimal(sys.argv[1])
        if isinstance(price, InvalidOperation):
            print("Incorrect value")
        else:
            print(format_price(price))
