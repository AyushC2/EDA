
df['SynergyIndex'] = df['Assists'] / df['FieldGoals']
df['WIN'] = df['WINorLOSS'].map({'W': 1, 'L': 0})
team_synergy = df.groupby('Team').agg({
    'SynergyIndex': 'mean',
    'WIN': 'mean'
}).reset_index()
team_synergy = team_synergy.rename(columns={'SynergyIndex': 'AST/FGA Ratio', 'WIN': 'Win %'})
plt.figure(figsize=(10, 6))
sns.scatterplot(data=team_synergy, x='AST/FGA Ratio', y='Win %', hue='Team', palette='tab10', s=100)

for i in range(len(team_synergy)):
    plt.text(x=team_synergy['AST/FGA Ratio'][i],
             y=team_synergy['Win %'][i],
             s=team_synergy['Team'][i],
             fontsize=9)

plt.title('Team Synergy: AST/FGA vs Win Percentage')
plt.xlabel('AST/FGA Ratio')
plt.ylabel('Win %')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
