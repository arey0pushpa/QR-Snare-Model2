import networkx as nx

G = nx.DiGraph()




#u = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7]
#v = [3, 4, 5, 0, 4, 5, 6, 1, 6, 7, 1, 7, 9, 6, 8, 4, 6, 5, 9, 9]

#w = zip(u,v)



w =  [(0,2),(0,2),(1,0),(1,0),(2,1)]


G.add_edges_from(w)

print(nx.is_strongly_connected(G))
print(nx.is_biconnected(G))












#basis = nx.simple_cycles(G)

#k = 0

 
#for i in basis :
#    k = k + 1
#    print(i)
    
#print("# elementary cycles are : ", k)



#print(nx.number_strongly_connected_components(G))

#print(' The strongly conncted subgraph')
#for h in nx.strongly_connected_components_recursive(G):
#   print h

#for i in G.edges():
 #   c = 0
 #   for path in nx.all_simple_paths(G,source=i[0], target=i[1]):
  #      c = c + 1
  #  if c == 1 :
  #      print(i) 



