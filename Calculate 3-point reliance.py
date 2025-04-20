
df['3Point_Ratio'] = df['X3PointShotsAttempted'] / df['FieldGoalsAttempted']
df['Date'] = pd.to_datetime(df['Date'])
df['MonthYear'] = df['Date'].dt.to_period('M')
grouped = df.groupby(['MonthYear', 'WINorLOSS'])[['3Point_Ratio', 'X3PointShots.']].mean().unstack()
plt.figure(figsize=(10, 6))
sns.heatmap(grouped['3Point_Ratio'], annot=True, fmt='.2f', cmap='Blues', cbar_kws={'label': '3-Point Ratio'})
plt.title('3-Point Reliance by Month')
plt.xlabel('Win/Loss')
plt.ylabel('Month-Year')
plt.show()
