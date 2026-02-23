# monthly-sales-trend.py
# Early 2022 - First marketing data project for Helit

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales-data.csv', parse_dates=['date'])
df['month'] = df['date'].dt.to_period('M')

monthly = df.groupby('month')['total_revenue'].sum().reset_index()
monthly['month'] = monthly['month'].astype(str)

plt.figure(figsize=(10, 6))
plt.plot(monthly['month'], monthly['total_revenue'], marker='o', linewidth=2.5)
plt.title('Monthly Revenue Trend - 2022')
plt.xlabel('Month')
plt.ylabel('Total Revenue (IRR)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('monthly-revenue-trend.png', dpi=150)
plt.show()
