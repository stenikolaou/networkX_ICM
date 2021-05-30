import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({
    "Graph 1": [485,572],
    "Graph 2": [410,394],
    "Graph 3": [867,854],
    "Graph 4": [31,39]
    },
    index=["Random seeds", "Max-centrality seeds"]
)

plotdata.plot(kind="bar", stacked=True)
plt.xticks(rotation=0, fontweight='bold', fontsize=16)
plt.yticks(fontweight='bold', fontsize=16)
plt.title("Total nodes infected per seed method", fontweight='bold', fontsize=22)
plt.ylabel("Total nodes infected", fontweight='bold', fontsize=18)

plt.show()




