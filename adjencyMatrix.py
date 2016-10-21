#!/usr/bin/python3.4
import ast


# edgelist_to_adjmatrix.py

def printMatrix(matrix):
    for i in range(len(matrix)):
        if (i == 0):
            print ('{')
        print('{',end='')
        for k in range(len(matrix[0])):
            if (k != (4)):                      # 2 is the n-1
                print(matrix[i][k], ",", end='')
            else:  
                print(matrix[i][k], end='')
        if (i != (len(matrix) - 1)):
             print('},',end='')
        else:
             print('}',end='')


    print('};')
#----------------------------------------------------------------

def main():

    with open("555.txt", "r") as f:
        for line in f.readlines():
            li = ast.literal_eval(line)
            edge_u = [x[0] for x in li]
            edge_v = [x[1] for x in li]
            print(edge_u)
            print(edge_v)
            print("\n")

    # our graph has n=10 nodes
            n = 5

            adjMatrix = [[0 for i in range(n)] for k in range(n)]


    # scan the arrays edge_u and edge_v
            for i in range(len(edge_u)):
                u = edge_u[i]
                v = edge_v[i]
                if adjMatrix[u][v] >= 1 :
                    adjMatrix[u][v] = adjMatrix[u][v] + 1
                else:
                    adjMatrix[u][v] = 1


    # check matrix
            print("Adjacency matrix: ")
            printMatrix(adjMatrix)
            print("\n")


#------------------------------------------------------------------
if __name__ == "__main__":
        main()
