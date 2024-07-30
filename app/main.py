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
    monthly_revenue.rename(columns={'product_price': 'revenue'}, inplace=True)
    return monthly_revenue


def compute_product_revenue(data):
    product_revenue = data.groupby('product_name')['product_price'].sum().reset_index()
    product_revenue.rename(columns={'product_price': 'revenue'}, inplace=True)
    return product_revenue


def compute_customer_revenue(data):
    customer_revenue = data.groupby('customer_id')['product_price'].sum().reset_index()
    customer_revenue.rename(columns={'product_price': 'revenue'}, inplace=True)
    return customer_revenue


def top_10_customers(data):
    customer_revenue = compute_customer_revenue(data)
    top_customers = customer_revenue.nlargest(10, 'revenue')
    return top_customers


def save_to_csv(data, filename):
    data.to_csv(filename, index=False)


def main():
    file_path = 'orders.csv'
    data = read_data(file_path)
    if data is not None:
        monthly_revenue = compute_monthly_revenue(data)
        product_revenue = compute_product_revenue(data)
        customer_revenue = compute_customer_revenue(data)
        top_customers = top_10_customers(data)

        print("Monthly Revenue:\n", monthly_revenue)
        print("Product Revenue:\n", product_revenue)
        print("Customer Revenue:\n", customer_revenue)
        print("Top 10 Customers:\n", top_customers)

        save_to_csv(monthly_revenue, 'monthly_revenue.csv')
        save_to_csv(product_revenue, 'product_revenue.csv')
        save_to_csv(customer_revenue, 'customer_revenue.csv')
        save_to_csv(top_customers, 'top_10_customers.csv')


if _name_ == "_main_":
    main()
