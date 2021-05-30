import networkx as nx
import matplotlib.pyplot as plt
import centrality_metrics as cm
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep

# Load data
fb=nx.read_edgelist("facebook.txt",create_using=nx.Graph(),nodetype=int)

# Get summary info
print(nx.info(fb))
#print("--------------------------------------------------")

# Plot graph
#nx.draw(fb)
#plt.show()

# Calculate centrality metrics
#cm.clustering_coefficient_f(fb)
#cm.closeness_centrality_f(fb)
#cm.closeness_centrality_max_f(fb)
#cm.eigenvector_centrality_f(fb)
#cm.betweenness_centrality_f(fb)
#cm.average_degree_connectivity_f(fb)

# Model selection
model = ep.IndependentCascadesModel(fb)
# Model Configuration
config = mc.Configuration()
config.add_model_parameter('fraction_infected', 0.01) # <---------------- pick seeds number as % of total nodes
# Setting the edge parameters
threshold = 0.1 # <----------------par2
for e in fb.edges([0]):
    config.add_edge_configuration("threshold", e, threshold)
model.set_initial_status(config)
list = []
# Simulation execution
for i in range(0,20):  # <----------------par3
    iterations = model.iteration_bunch(1)
    print(iterations)
#------------------------------------------------------------------------------
    dict = iterations[0]
    for i in dict:
        k = (i, dict[i])
        list.append(k)
#------------------------------------------------------------------------------
list2 = []
for i in range(len(list)):
    if list[i][0] == 'status':
        list2.append(list[i][1])
list4 = []
for t in range(len(list2)):
    for f in list2[t]:
        #print(f , ':' , list2[t][f])
        if list2[t][f] == 1:
            list4.append(f)
print("Total nodes infected: ", len(list4))
print("Percentage  of total infected nodes with current seed set: ", (len(list4)/len(nx.nodes(fb)))*100,"%")




