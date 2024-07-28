import pandas as pd

def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading the data: {e}")
        return None

def compute_monthly_revenue(data):
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['month'] = data['order_date'].dt.to_period('M')
    monthly_revenue = data.groupby('month')['product_price'].sum().reset_index()
    return monthly_revenue

def compute_product_revenue(data):
    product_revenue = data.groupby('product_name')['product_price'].sum().reset_index()
    return product_revenue

def compute_customer_revenue(data):
    customer_revenue = data.groupby('customer_id')['product_price'].sum().reset_index()
    return customer_revenue

def top_10_customers(data):
    customer_revenue = compute_customer_revenue(data)
    top_customers = customer_revenue.nlargest(10, 'product_price')
    return top_customers

def main():
    file_path = 'orders.csv'
    data = read_data(file_path)
    if data is not None:
        print("Monthly Revenue:\n", compute_monthly_revenue(data))
        print("Product Revenue:\n", compute_product_revenue(data))
        print("Customer Revenue:\n", compute_customer_revenue(data))
        print("Top 10 Customers:\n", top_10_customers(data))

if __name__ == "__main__":
    main()
