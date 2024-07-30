import unittest
import pandas as pd
from app.main import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_10_customers

class TestMain(unittest.TestCase):

    def setUp(self):
        data = {
            'order_date': ['2021-01-01', '2021-01-15', '2021-02-01', '2021-02-20', '2021-03-01'],
            'customer_id': [1, 2, 1, 3, 2],
            'product_name': ['A', 'B', 'A', 'C', 'B'],
            'product_price': [100, 200, 150, 300, 250]
        }
        self.df = pd.DataFrame(data)

    def test_compute_monthly_revenue(self):
        result = compute_monthly_revenue(self.df)
        expected_data = {
            'month': ['2021-01', '2021-02', '2021-03'],
            'revenue': [300, 450, 250]
        }
        expected = pd.DataFrame(expected_data)
        expected['month'] = pd.PeriodIndex(expected['month'], freq='M')
        pd.testing.assert_frame_equal(result, expected)

    def test_compute_product_revenue(self):
        result = compute_product_revenue(self.df)
        expected_data = {
            'product_name': ['A', 'B', 'C'],
            'revenue': [250, 450, 300]
        }
        expected = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected)

    def test_compute_customer_revenue(self):
        result = compute_customer_revenue(self.df)
        expected_data = {
            'customer_id': [1, 2, 3],
            'revenue': [250, 450, 300]
        }
        expected = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected)

    def test_top_10_customers(self):
        result = top_10_customers(self.df)
        expected_data = {
            'customer_id': [2, 3, 1],
            'revenue': [450, 300, 250]
        }
        expected = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

if _name_ == '_main_':
    unittest.main()
