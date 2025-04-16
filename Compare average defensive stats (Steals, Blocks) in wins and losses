

plt.figure(figsize=(8, 5))
sns.barplot(x='WINorLOSS', y='Steals', data=df, errorbar=('ci', 95), label='Steals', color='skyblue')
sns.barplot(x='WINorLOSS', y='Blocks', data=df, errorbar=('ci', 95), label='Blocks', color='lightgreen', alpha=0.7)
plt.title('Steals and Blocks in Wins vs Losses')
plt.ylabel('Average Count')
plt.xticks([0, 1], ['Loss', 'Win'])
plt.legend()
plt.tight_layout()
plt.show()
