import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):

    def test_trailing_zeros_value(self):
        formatted_price = format_price('123456789.00000000000')
        self.assertEqual(formatted_price, '123 456 789')

    def test_input_integer_string(self):
        formatted_price = format_price('123456789')
        self.assertEqual(formatted_price, '123 456 789')

    def test_input_float_string(self):
        formatted_price = format_price('123456.93333')
        self.assertEqual(formatted_price, '123 456.93')

    def test_round_half_up(self):
        formatted_price = format_price('123456.5555')
        self.assertEqual(formatted_price, '123 456.56')

    def test_input_incorrect_value(self):
        formatted_price = format_price('12345.ABC')
        self.assertIsNone(formatted_price)


if __name__ == '__main__':
    unittest.main()
