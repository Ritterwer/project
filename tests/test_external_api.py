import unittest
from unittest.mock import patch

from src.external_api import currency_conversion


class TestCurrencyConversion(unittest.TestCase):
    @patch("requests.get")
    def test_conversion_valid(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 7500.0}
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
        result = currency_conversion(transaction)
        self.assertEqual(result, 7500.0)

    def test_conversion_invalid(self):
        transaction_info = {"operationAmount": {"amount": None, "currency": {"code": None}}}
        with self.assertRaises(ValueError):
            currency_conversion(transaction_info)
