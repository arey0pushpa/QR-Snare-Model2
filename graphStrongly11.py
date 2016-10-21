import networkx as nx
import ast

G = nx.DiGraph()
n = 5

#u = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]
#v = [1, 3, 4, 8, 9, 2, 3, 4, 6, 8, 9, 5, 6, 8, 4, 7, 0, 2, 3, 6, 7, 1, 8, 1, 4, 0, 3, 5, 6, 0, 1, 4, 7]
#w = zip(u,v)
#w = [(0,1),(0,6), (1,2), (1,3), (1,9), (2,0) ,(2,5), (2,7),(3,0),(3,2), (4,0), (4,3),(4,5),(5,4),(5,8),(5,9),(5,9),(6,7),(6,9),(7,1),(7,8),(8,4),(8,9),(9,4),(9,6)]



with open("55.txt", "r") as f:
        for line in f.readlines():
            li = ast.literal_eval(line)
            w = li
            G = nx.DiGraph()
            G.add_edges_from(w)
            count = 0
            if(nx.is_strongly_connected(G)) :
                #print nx.degree(G)
                C1 = True
                C2 = False
                cond = 0
                for i in range(0,n):
                    c = 0
                    e1 = [x[0] for x in w]
                    e2 = [x[1] for x in w]
                    for j in e1 :
                        if (i == j):
                            c = c + 1
                    for k in e2 :
                        if (i == k):
                            c = c + 1
                    if (c >= 3):
                        C1 = C1 and True
                    else:
                        C1 = False
                    if ( c < 4) :
                        C2 = True
                if ((C1 == True) and  (C2 == True)):
                    print w





