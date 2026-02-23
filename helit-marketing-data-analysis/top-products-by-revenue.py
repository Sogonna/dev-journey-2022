# top-products-by-revenue.py
# Early 2022

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales-data.csv')

top_products = df.groupby('product_name')['total_revenue'].sum().nlargest(10)

plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='#4c72b0')
plt.title('Top 10 Best-Selling Products by Revenue (2022)')
plt.ylabel('Total Revenue')
plt.xlabel('Product Name')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('top-10-products.png', dpi=150)
plt.show()

