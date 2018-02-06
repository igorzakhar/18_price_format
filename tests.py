import unittest
from decimal import InvalidOperation

from format_price import format_price, convert_to_decimal


class FormatPriceTestCase(unittest.TestCase):

    def test_trailing_zeros_value(self):
        price = convert_to_decimal('123456789.00000000000')
        formatted_price = format_price(price)
        self.assertEqual(formatted_price, '123 456 789')

    def test_input_integer_string(self):
        price = convert_to_decimal('123456789')
        formatted_price = format_price(price)
        self.assertEqual(formatted_price, '123 456 789')

    def test_input_float_string(self):
        price = convert_to_decimal('123456.93333')
        formatted_price = format_price(price)
        self.assertEqual(formatted_price, '123 456.93')

    def test_round_half_up(self):
        price = convert_to_decimal('123456.5555')
        formatted_price = format_price(price)
        self.assertEqual(formatted_price, '123 456.56')

    def test_convert_invalid_value(self):
        price = convert_to_decimal('123456.abc')
        self.assertIsInstance(price, InvalidOperation)

    def test_format_invalid_value(self):
        with self.assertRaises(ValueError):
            format_price('123456789')


if __name__ == '__main__':
    unittest.main()
