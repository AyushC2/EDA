#Objective3: Analyze the Impact of Home vs. Away Games on Winning Percentage

home_win_rate = df.groupby('Home')['WIN'].mean()
labels = ['Away Win Rate', 'Home Win Rate']
sizes = home_win_rate.values
colors = ['#ff9999', '#66b3ff']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90, colors=colors)
plt.title('Win Rate Distribution: Home vs Away')
plt.axis('equal')

plt.tight_layout()
plt.show()
