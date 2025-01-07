import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.transaction_file import read_financial_operations_from_csv, read_financial_operations_from_excel


class TestFinancialOperations(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='column1,column2\nvalue1,value2\n')
    def test_read_financial_operations_from_csv(self, mock_file):
        transactions = read_financial_operations_from_csv('dummy.csv')
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['column1'], 'value1')
        self.assertEqual(transactions[0]['column2'], 'value2')
        mock_file.assert_called_once_with('dummy.csv', mode='r', encoding='utf-8')

    @patch("pandas.read_excel")
    def test_read_financial_operations_from_excel(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({"column1": ["value1"], "column2": ["value2"]})
        transactions = read_financial_operations_from_excel("dummy.xlsx")
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["column1"], "value1")
        self.assertEqual(transactions[0]["column2"], "value2")


if __name__ == "__main__":
    unittest.main()
