# customer-rfm-segmentation-2022.py
# Late 2022 - Customer Segmentation using RFM Analysis


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load data
df = pd.read_csv('customer-data.csv', parse_dates=['last_purchase_date'])

# RFM Calculation
snapshot_date = datetime(2023, 4, 1)

rfm = df.groupby('customer_id').agg({
    'last_purchase_date': lambda x: (snapshot_date - x.max()).days,   
    'frequency': 'max',                                               
    'monetary': 'sum'                                                 
}).rename(columns={
    'last_purchase_date': 'Recency',
    'frequency': 'Frequency',
    'monetary': 'Monetary'
}).reset_index()

# RFM Scoring (1-5 scale) 
rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_score'] = pd.qcut(rfm['Frequency'], 5, labels=[1, 2, 3, 4, 5])
rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

rfm['RFM_Score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)

# Customer Segments
segment_map = {
    r'5[4-5][4-5]': 'Champions',
    r'5[3-5][1-3]': 'Loyal Customers',
    r'[3-4][3-5][3-5]': 'Potential Loyalist',
    r'[1-2][4-5][4-5]': 'New Customers',
    r'[1-2][1-2][1-2]': 'At Risk',
    r'[1-2][1-5][1-5]': 'Hibernating',
    r'5[1-2][1-5]': 'Promising',
    r'[3-4][1-2][1-5]': 'Need Attention'
}

rfm['Segment'] = rfm['RFM_Score'].replace(segment_map, regex=True)

# Analysis & Insights-
print("=== RFM Analysis Summary (2022) ===")
print(f"Total Customers: {len(rfm)}")
print("\nSegment Distribution:")
print(rfm['Segment'].value_counts().sort_values(ascending=False))

print("\nAverage Monetary Value per Segment:")
print(rfm.groupby('Segment')['Monetary'].mean().round(0).sort_values(ascending=False))

#Visualizations
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Scatter Plot
scatter = axes[0].scatter(rfm['Recency'], rfm['Monetary'], 
                         c=rfm['Frequency'], cmap='plasma', s=60, alpha=0.8)
axes[0].set_title('RFM Scatter Plot - Customer Value Overview')
axes[0].set_xlabel('Recency (days since last purchase)')
axes[0].set_ylabel('Monetary Value (Total Spent)')
plt.colorbar(scatter, ax=axes[0], label='Frequency')

# Segment Bar Chart
segment_counts = rfm['Segment'].value_counts()
segment_counts.plot(kind='bar', ax=axes[1], color=sns.color_palette("viridis", len(segment_counts)))
axes[1].set_title('Customer Segments Distribution')
axes[1].set_ylabel('Number of Customers')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()

plt.savefig('rfm-advanced-segmentation.png', dpi=180, bbox_inches='tight')
plt.show()

