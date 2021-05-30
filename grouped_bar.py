import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("bar.csv")
df.set_index('Graph')

#plt.style.use('dark_background')

fig = plt.figure() # Create matplotlib figure
ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.
width = 0.4
df.plot(kind='bar', x = 'Graph', y = 'Clustering', color='orange', ax=ax, width=width, position=1)
df.plot(kind='bar', x = 'Graph', y = 'Degree', color='grey', ax=ax2, width=width, position=0)

ax.set_title("Clustering coefficient and degree per graph", fontsize=24, fontweight='bold')
ax.set_xlabel('Graphs', fontsize=18, fontweight='bold', labelpad=10)
ax.set_ylabel('Average clustering coefficient', fontsize=18, fontweight='bold', labelpad=10)
ax2.set_ylabel('Average degree',  fontsize=18, fontweight='bold', labelpad=10)
ax.tick_params(axis='x', rotation=45)
plt.setp(ax.get_xticklabels(), fontsize=16, fontweight="bold")
plt.setp(ax.get_yticklabels(), fontsize=16, fontweight="bold")
plt.setp(ax2.get_yticklabels(), fontsize=16, fontweight="bold")
ax.legend(loc='upper left', fontsize=14)
ax2.legend(loc='best', fontsize=14)
plt.show()


