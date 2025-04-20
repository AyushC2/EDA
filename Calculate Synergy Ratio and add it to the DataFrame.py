
df['Win'] = df['WINorLOSS'].map({'W': 1, 'L': 0})
home_away_winrate = df.groupby('Home')['Win'].mean().reset_index()

home_wins = df[df['Home'] == 'Home']['Win']
away_wins = df[df['Home'] == 'Away']['Win']
t_stat, p_val = ttest_ind(home_wins, away_wins, equal_var=False)
plt.figure(figsize=(8, 6))
sns.barplot(data=home_away_winrate, x='Home', y='Win')
plt.title('Win Percentage: Home vs Away')
plt.ylabel('Average Win Rate')
plt.xlabel('Game Location')
plt.text(0.5, max(home_away_winrate['Win']) * 0.95,
         f'p-value = {p_val:.4f}\nT-stat = {t_stat:.2f}',
         ha='center', fontsize=10, color='darkred')
plt.tight_layout()
plt.show()
print("Hypothesis Test: Home Court Advantage")
print(f"T-statistic = {t_stat:.4f}")
print(f"P-value = {p_val:.4f}")

if p_val < 0.05:
    print(" Result: Statistically significant. Home teams have a higher win rate.")
else:
    print("Result: Not statistically significant. No clear home court advantage.")
