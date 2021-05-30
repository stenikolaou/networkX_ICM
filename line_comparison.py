import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("line_comparison.csv")
df.set_index('Graph', inplace=True)

# Build plot
df['Random seeds'].plot(figsize = (16,9), legend=True, marker='o')
df['Max-centrality seeds'].plot(figsize = (16,9), legend=True, marker='o')
plt.title("Information propagation per initial seed choice", fontweight ='bold', fontsize=24, color='black')
plt.xlabel('Random graph', fontweight ='bold', fontsize=18, color='black')
plt.ylabel('Percentage of nodes infected', fontweight ='bold', fontsize=18, color='black')
plt.xticks(fontweight ='bold')
plt.yticks(fontweight ='bold')
plt.show()