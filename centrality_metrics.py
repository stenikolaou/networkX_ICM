import networkx as nx

# =================================== Calculate average clustering coefficient =========================================
def clustering_coefficient_f(data):
    cl = nx.clustering(data)
    ls = []
    for x in cl:
        ls.append(cl[x])
    clust = sum(ls) / len(ls)
    print('Average clustering coefficient: ', clust)

    # Find the node with max clustering coefficient

    max = 0
    for x in cl:
        if cl[x] >= max:
            max = cl[x]

    cnt = []
    for y in cl:
        if cl[y] == max:
            cnt.append(y)
    print("Max value: ", max)
    print("Nodes:", cnt)
    print("==================================================")

# =================================== Calculate average closeness ======================================================
def closeness_centrality_f(data):
    clon = nx.closeness_centrality(data)
    lscl = []
    for y in clon:
        lscl.append(clon[y])
    clon = sum(lscl) / len(lscl)
    print('Average Closeness: ', clon)

# Find the node with max closeness
def closeness_centrality_max_f(datafb):
    clon = nx.closeness_centrality(datafb)
    max = 0
    for y in clon:
        if clon[y] >= max:
            max = clon[y]
    cnt = []
    for z in clon:
        if clon[z] == max:
            cnt.append(z)
    print("Max value: ", max)
    print("Nodes:", cnt)
    print("==================================================")
# --------------------------------------------------------------------------
# Calculate average eigenvector centrality
def eigenvector_centrality_f(data):
    ec = nx.eigenvector_centrality(data, max_iter=500)
    ecl = []
    for y in ec:
        ecl.append(ec[y])
    ecsum = sum(ecl) / len(ecl)
    print('Eigenvector Centrality: ', ecsum)

    # Find the node with max eigenvector centrality
    max = 0
    for x in ec:
        if ec[x] >= max:
            max = ec[x]

    cnt = []
    for y in ec:
        if ec[y] == max:
            cnt.append(y)
    print("Max value: ", max)
    print("Nodes:", cnt)
    print("==================================================")
# --------------------------------------------------------------------------
# Calculate average betweenness centrality
def betweenness_centrality_f(data):
    bc = nx.betweenness_centrality(data)
    bcl = []
    for y in bc:
        bcl.append(bc[y])
    bcsum = sum(bcl) / len(bcl)
    print('Betweenness Centrality: ', bcsum)
    # Find the node with max betweenness
    max = 0
    for x in bc:
        if bc[x] >= max:
            max = bc[x]

    cnt = []
    for y in bc:
        if bc[y] == max:
            cnt.append(y)

    print("Max value: ", max)
    print("Nodes:", cnt)
    print("==================================================")
# --------------------------------------------------------------------------
# Calculate average degree
def average_degree_connectivity_f(data):
    ad = nx.degree(data)
    adl = []
    for y in range(len(ad)):
        adl.append(ad[y])
    adsum = sum(adl) / len(adl)
    print('Average Degree: ', adsum)

    # Find the node with max degree
    max = 0
    for x in range(len(ad)):
        if ad[x] >= max:
            max = ad[x]

    cnt = []
    for y in range(len(ad)):
        if ad[y] == max:
            cnt.append(y)

    print("Max value: ", max)
    print("Nodes:", cnt)
    print("==================================================")

def ranking_formula(datagr , p):#1-degree #2-clustering #3-betweenness #4-eigenvector
    ad = datagr.degree
    cl = nx.clustering(datagr)
    bc = nx.betweenness_centrality(datagr)
    ec = nx.eigenvector_centrality(datagr, max_iter=500)
    frank = []
    frankall = []
    if(p == 'y'):
        for z in range(len(cl)):
            frank.append(str(z) + '|' + str(ad[z] + cl[z] + bc[z] + ec[z]))
        return frank
    if(p == 'n'):
        for l in range(len(cl)):
            frankall.append(str(l) + '|' + str(ad[l]) + '|' + str(cl[l]) + '|' + str(bc[l]) + '|' + str(ec[l]))
        return frankall


