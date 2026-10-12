# import requests
# import pandas as pd

# # 1. Get the data from the website
# print("Downloading data...")
# url = "https://fakestoreapi.com/products"
# response = requests.get(url)
# data = response.json()

# # 2. Convert the raw data into a table (called a DataFrame in pandas)
# print("Converting to a table...")
# df = pd.DataFrame(data)

# # 3. Save the table as a CSV file on your laptop
# df.to_csv("my_data.csv", index=False)
# print("Success! Open my_data.csv to see your data.")

000 

# import requests
# import pandas as pd
# from datetime import datetime

# print("Downloading data...")
# url = "https://fakestoreapi.com/products"
# response = requests.get(url)
# data = response.json()

# print("Converting to a table...")
# df = pd.DataFrame(data)

# print("Cleaning the data...")
# # 1. Filter: Keep only the columns we need for the dashboard
# clean_df = df[['id', 'title', 'category', 'price']].copy()

# # 2. Add new data: Create a column for today's date
# clean_df['report_date'] = datetime.now().strftime("%Y-%m-%d")

# # 3. Save the clean version to a brand new file
# clean_df.to_csv("clean_data.csv", index=False)
# print("Success! Open clean_data.csv to see the business-ready data.")


import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Fetching base products...")
url = "https://fakestoreapi.com/products"
products = requests.get(url).json()

print("Simulating 1,000 sales transactions...")
np.random.seed(42)
records = []
start_date = datetime.now() - timedelta(days=30)

for transaction_id in range(1, 1001):
    product = np.random.choice(products)
    quantity = int(np.random.randint(1, 6))
    random_days = int(np.random.randint(0, 31))
    sale_date = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
    
    records.append({
        "transaction_id": transaction_id,
        "product_id": product["id"],
        "title": product["title"],
        "category": product["category"],
        "unit_price": product["price"],
        "quantity": quantity,
        "total_revenue": round(product["price"] * quantity, 2),
        "sale_date": sale_date
    })

df_sales = pd.DataFrame(records)
df_sales.to_csv("clean_data.csv", index=False)
print("Success! Created 1,000 transaction rows in clean_data.csv.")