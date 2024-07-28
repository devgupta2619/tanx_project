import unittest
import pandas as pd
from app.main import read_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_10_customers

class TestMain(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'order_id': [1, 2, 3],
            'customer_id': [1, 2, 1],
            'order_date': ['2023-01-01', '2023-01-10', '2023-02-01'],
            'product_id': [1, 2, 1],
            'product_name': ['Product A', 'Product B', 'Product A'],
            'product_price': [100, 200, 150],
            'quantity': [1, 1, 1]
        })

    def test_compute_monthly_revenue(self):
        result = compute_monthly_revenue(self.data)
        expected = pd.DataFrame({'month': ['2023-01', '2023-02'], 'product_price': [300, 150]})
        pd.testing.assert_frame_equal(result, expected)

    def test_compute_product_revenue(self):
        result = compute_product_revenue(self.data)
        expected = pd.DataFrame({'product_name': ['Product A', 'Product B'], 'product_price': [250, 200]})
        pd.testing.assert_frame_equal(result, expected)

    def test_compute_customer_revenue(self):
        result = compute_customer_revenue(self.data)
        expected = pd.DataFrame({'customer_id': [1, 2], 'product_price': [250, 200]})
        pd.testing.assert_frame_equal(result, expected)

    def test_top_10_customers(self):
        result = top_10_customers(self.data)
        expected = pd.DataFrame({'customer_id': [1, 2], 'product_price': [250, 200]}).nlargest(10, 'product_price')
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
