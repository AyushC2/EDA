# Objective 1: Show correlation between performance metrics

features = ['TeamPoints', 'FieldGoals', 'X3PointShots', 'FreeThrows', 'TotalRebounds', 'Assists', 'Steals', 'Blocks', 'Turnovers', 'TotalFouls', 'WIN']
corr = df[features].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Game Features')
plt.tight_layout()
plt.show()
