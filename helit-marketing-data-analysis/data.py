# create_sample_data_2022.py
# این فایل رو اجرا کن تا سه CSV ساخته شود

import pandas as pd
import numpy as np
from datetime import datetime

np.random.seed(42)

# ۱. sales_data_2022.csv
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
n_rows = 4000

sales_df = pd.DataFrame({
    'date': np.random.choice(dates, n_rows),
    'product_name': np.random.choice(['T-Shirt Basic', 'Hoodie Oversize', 'Jeans Slim', 'Dress Summer', 'Jacket Leather', 'Scarf Wool'], n_rows),
    'category': np.random.choice(['T-Shirt', 'Hoodie', 'Jeans', 'Dress', 'Jacket', 'Accessory'], n_rows),
    'quantity': np.random.randint(1, 6, n_rows),
    'unit_price': np.random.uniform(250000, 1800000, n_rows).round(0),
    'customer_id': np.random.randint(1001, 3001, n_rows)
})

sales_df['total_revenue'] = (sales_df['quantity'] * sales_df['unit_price']).round(0)
sales_df.to_csv('sales-data.csv', index=False, encoding='utf-8-sig')
print("sales_data_2022.csv ساخته شد →", sales_df.shape)

# ۲. campaign_data_2022.csv
campaigns = [
    {'campaign_name': 'Instagram Summer Sale', 'channel': 'Instagram', 'start_date': '2022-06-01', 'end_date': '2022-06-15', 'budget': 45000000, 'revenue_generated': 128000000, 'clicks': 14500, 'conversions': 820},
    {'campaign_name': 'New Year Discount', 'channel': 'Telegram', 'start_date': '2022-12-20', 'end_date': '2023-01-05', 'budget': 32000000, 'revenue_generated': 89000000, 'clicks': 9800, 'conversions': 610},
    {'campaign_name': 'Google Back-to-School', 'channel': 'Google Ads', 'start_date': '2022-08-10', 'end_date': '2022-09-05', 'budget': 68000000, 'revenue_generated': 210000000, 'clicks': 24500, 'conversions': 1450},
    {'campaign_name': 'Black Friday Flash', 'channel': 'Instagram', 'start_date': '2022-11-20', 'end_date': '2022-11-28', 'budget': 85000000, 'revenue_generated': 315000000, 'clicks': 38000, 'conversions': 2200},
    {'campaign_name': 'Email Birthday Promo', 'channel': 'Email', 'start_date': '2022-03-01', 'end_date': '2022-03-31', 'budget': 12000000, 'revenue_generated': 42000000, 'clicks': 5200, 'conversions': 340},
]

pd.DataFrame(campaigns).to_csv('campaign-data.csv', index=False, encoding='utf-8-sig')
print("campaign_data_2022.csv ساخته شد")

# ۳. customer_data_2022.csv
n_customers = 1800
customer_df = pd.DataFrame({
    'customer_id': range(1001, 1001 + n_customers),
    'last_purchase_date': pd.to_datetime(np.random.choice(pd.date_range('2022-01-01', '2023-03-31'), n_customers)),
    'frequency': np.random.randint(1, 18, n_customers),
    'monetary': np.random.uniform(450000, 12500000, n_customers).round(0)
})

customer_df.to_csv('customer-data.csv', index=False, encoding='utf-8-sig')
print("customer_data_2022.csv ساخته شد →", customer_df.shape)