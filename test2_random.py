import networkx as nx
import matplotlib.pyplot as plt
import centrality_metrics as cm
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep

r2=nx.read_gml("random2.gml")

# =================================== Get summary info =================================================================
#print(nx.info(r2))
#print("===========================================================")

# =================================== Plot graph =======================================================================
#nx.draw(r2,with_labels=True)
#plt.show()

# =================================== Calculate centrality metrics =====================================================
#cm.clustering_coefficient_f(r2)
#cm.closeness_centrality_f(r2)
#cm.closeness_centrality_max_f(r2)
#cm.eigenvector_centrality_f(r2)
#cm.betweenness_centrality_f(r2)
#cm.average_degree_connectivity_f(r2)

# =================================== Independent Cascade Model ========================================================
model = ep.IndependentCascadesModel(r2)

# Model Configuration
config = mc.Configuration()
config.add_model_parameter('fraction_infected', 0.05)  # <---------------- Define seeds as percentage of total nodes

# Setting the edge parameters
threshold = 0.1  # <---------------- Infection probability
for e in r2.edges():
    config.add_edge_configuration("threshold", e, threshold)
model.set_initial_status(config)
list = []

# Simulation execution
for i in range(0, 40):  # <---------------- Number of model iterations
    iterations = model.iteration_bunch(1)
    #print(iterations)

# Get infected nodes
    dict = iterations[0]
    for i in dict:
        k = (i, dict[i])
        list.append(k)

list2 = []
for i in range(len(list)):
    if list[i][0] == 'status':
        list2.append(list[i][1])
list4 = []
for t in range(len(list2)):
    for f in list2[t]:
        # print(f , ':' , list2[t][f])
        if list2[t][f] == 1:
            list4.append(f)
#print(list4)
print("===============================================================================================================")
print("Total nodes infected: ", len(list4), "out of", len(nx.nodes(r2)))
print("Percentage  of total infected nodes with current seed set: ", (len(list4)/len(nx.nodes(r2)))*100,"%")
print("===============================================================================================================")

# =================================== Get seeds list ===================================================================
list3 = []
for i in range(len(list)):
    if list[i][0] == 'status':
        list3.append(list[i][1])

# print(list3[0])
z = str(list3[0])
a = z.replace('{', '')
b = a.replace('}', '')
dirtlist = b.split(',')
clearlist = []
for q in range(len(dirtlist)):
    clearlist.append(dirtlist[q].replace(' ', ''))
infectedlist = []
for w in range(len(clearlist)):
    if (clearlist[w].split(':')[1] == '1'):
        infectedlist.append(clearlist[w].split(':')[0])

# Seeds list
print("Total seeds:", len(infectedlist))
print("Seeds set:", infectedlist)
print("===============================================================================================================")
