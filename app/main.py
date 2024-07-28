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

def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
    print(f"Saved {filename}")

def main():
    file_path = 'orders.csv'
    data = read_data(file_path)
    if data is not None:
        monthly_revenue = compute_monthly_revenue(data)
        save_to_csv(monthly_revenue, 'monthly_revenue.csv')
        
        product_revenue = compute_product_revenue(data)
        save_to_csv(product_revenue, 'product_revenue.csv')
        
        customer_revenue = compute_customer_revenue(data)
        save_to_csv(customer_revenue, 'customer_revenue.csv')
        
        top_customers = top_10_customers(data)
        save_to_csv(top_customers, 'top_10_customers.csv')

if _name_ == "_main_":
    main()