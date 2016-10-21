import networkx as nx
import ast

G = nx.DiGraph()

#u = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]
#v = [1, 3, 4, 8, 9, 2, 3, 4, 6, 8, 9, 5, 6, 8, 4, 7, 0, 2, 3, 6, 7, 1, 8, 1, 4, 0, 3, 5, 6, 0, 1, 4, 7]
#w = zip(u,v)
#w = [(0,1),(0,6), (1,2), (1,3), (1,9), (2,0) ,(2,5), (2,7),(3,0),(3,2), (4,0), (4,3),(4,5),(5,4),(5,8),(5,9),(5,9),(6,7),(6,9),(7,1),(7,8),(8,4),(8,9),(9,4),(9,6)] 

with open("makeGraphs.txt", "r") as f:
        for line in f.readlines():
            li = ast.literal_eval(line)
            w = li 
            G = nx.DiGraph()
            G.add_edges_from(w)
            if(nx.is_strongly_connected(G)) :
                print(line)
                for i in G.edges():
                    c = 0
                    for path in nx.all_simple_paths(G,source=i[0], target=i[1]):
                        c = c + 1
                    if c == 1 :
                        print(i) 
                    print(" One ends: \n") 
               



