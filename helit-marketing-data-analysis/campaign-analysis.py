# campaign-roi-analysis.py
# Mid-late 2022 - Real business metric calculation "Helit"

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('campaign-data.csv')

df['ROI'] = ((df['revenue_generated'] - df['budget']) / df['budget']) * 100
df['ROAS'] = df['revenue_generated'] / df['budget']

print("Campaign Performance Summary:")
print(df[['campaign_name', 'channel', 'budget', 'revenue_generated', 'ROI', 'ROAS']].round(2))

# Visualization
plt.figure(figsize=(11, 6))
channels = df.groupby('channel')['ROI'].mean().sort_values()
channels.plot(kind='bar', color=['#55a868', '#c44e52', '#8172b3', '#4c72b0'])
plt.title('Average ROI by Marketing Channel (2022)')
plt.ylabel('ROI (%)')
plt.axhline(0, color='red', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('campaign-roi-by-channel.png', dpi=150)
plt.show()

