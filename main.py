import pandas as pd
from sqlalchemy import create_engine

# Step 1: Read the Excel file
file_path = 'GlobalSuper.xlsx'  # Replace with your actual file path
data = pd.read_excel(file_path)

# Step 2: Normalize the data
# Normalization means breaking down the large table into smaller ones with relationships (like customers, orders, products, etc.)

# Extracting unique customers
customers = data[['Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Country', 'Postal Code', 'Region']].drop_duplicates()

# Extracting unique products
products = data[['Product ID', 'Category', 'Sub-Category', 'Product Name']].drop_duplicates()

# Extracting unique orders
orders = data[['Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Order Priority']].drop_duplicates()

# Extracting sales data (fact table)
sales_data = data[['Order ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost']]

# Step 3: Insert normalized tables into MySQL
# Define your MySQL database credentials
db_config = {
    'user': 'root',        # Replace with your MySQL username
    'password': '12345',    # Replace with your MySQL password
    'host': 'localhost',
    'database': 'gloablSuperStore' # Replace with your MySQL database name
}

# Create a SQLAlchemy engine to connect to MySQL
engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Insert data into MySQL
customers.to_sql('customers', engine, index=False, if_exists='replace')  # Insert customer data
products.to_sql('products', engine, index=False, if_exists='replace')    # Insert product data
orders.to_sql('orders', engine, index=False, if_exists='replace')        # Insert order data
sales_data.to_sql('sales_data', engine, index=False, if_exists='replace') # Insert sales data

print("Data normalized and inserted into MySQL database successfully!")
