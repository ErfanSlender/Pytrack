import unittest
from main import calculate_balance

class TestCalculateBalance(unittest.TestCase):
    def test_balance(self):
        transactions = [
            {'Type': 'Income',
             'Amount': 1000},
            {'Type': 'Expense',
             'Amount': 300},
            {'Type': 'Income',
             'Amount': 500}
        ]
        
        result = calculate_balance(transactions)
        self.assertEqual(result, 1200)

if __name__ == '__main__':
    unittest.main()