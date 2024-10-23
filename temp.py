import mysql.connector
import pandas as pd

# MySQL connection setup
conn = mysql.connector.connect(
    host='localhost',  # Your MySQL server host
    user='root',  # Your MySQL username
    password='12345',  # Your MySQL password
    database='GlobalStoreSalesDB'  # Your MySQL database name
)


# Queries to fetch data from tables
query_customers = "SELECT * FROM Customers"
query_products = "SELECT * FROM Products"
query_orders = "SELECT * FROM Orders"

# Load data into pandas DataFrames
df_customers = pd.read_sql(query_customers, conn)
df_products = pd.read_sql(query_products, conn)
df_orders = pd.read_sql(query_orders, conn)

# Create a writer object to write to Excel
with pd.ExcelWriter('database_export.xlsx', engine='openpyxl') as writer:
    df_customers.to_excel(writer, sheet_name='Customers', index=False)
    df_products.to_excel(writer, sheet_name='Products', index=False)
    df_orders.to_excel(writer, sheet_name='Orders', index=False)

# Close the MySQL connection
conn.close()

print("Data exported to 'database_export.xlsx'")
