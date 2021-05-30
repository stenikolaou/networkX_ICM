import networkx as nx
import centrality_metrics as cm

# Create random graphs
r1=nx.barabasi_albert_graph(2736,3)
r2=nx.barabasi_albert_graph(859,6)
r3=nx.barabasi_albert_graph(1117,11)
r4=nx.barabasi_albert_graph(137,4)

# Save random graphs to gml file
nx.write_gml(r1, "random1.gml")
nx.write_gml(r2, "random2.gml")
nx.write_gml(r3, "random3.gml")
nx.write_gml(r4, "random4.gml")

# Print summary
print(nx.info(r1))
print(nx.info(r2))
print(nx.info(r3))
print(nx.info(r4))

# Print clustering coefficient
cm.clustering_coefficient_f(r1)
cm.clustering_coefficient_f(r2)
cm.clustering_coefficient_f(r3)
cm.clustering_coefficient_f(r4)