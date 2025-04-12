# Objective 2: Identify Outliers in Team Performance Based on Points Scored
Q1 = df['TeamPoints'].quantile(0.25)
Q3 = df['TeamPoints'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
outliers = df[(df['TeamPoints'] < lower_bound) | (df['TeamPoints'] > upper_bound)]
outlier_count = len(outliers)
plt.figure(figsize=(6, 8))
sns.boxplot(y=df['TeamPoints'], color='orange')
plt.title('Outliers in Team Points Scored')
plt.ylabel('Points Scored')

plt.text(0.05, df['TeamPoints'].max() - 1, f'OutliersCount: {outlier_count}', fontsize=12, color='#333335')

plt.tight_layout()
plt.show()
