import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('nba_games_stats.csv')
# Pre-analysis inspection
print("Missing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)
print("\nUnique values in 'Home':", df['Home'].unique())
print("Unique values in 'WINorLOSS':", df['WINorLOSS'].unique())
print("\nPreview:\n", df.head())
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Opp.TotalFouls'] = pd.to_numeric(df['Opp.TotalFouls'], errors='coerce')
df['Opp.TotalFouls'].fillna(df['Opp.TotalFouls'].median(), inplace=True)
plt.figure(figsize=(14,10))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
# Distribution of numerical features
df.select_dtypes(include=np.number).hist(bins=20,figsize=(16, 10), color='skyblue')
plt.suptitle("Distribution of Numerical Features")
plt.tight_layout()
plt.show()
