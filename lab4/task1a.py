import numpy as np

def createAdjacencyMatrix(vertices, edges):
    adj_matrix = np.zeros((vertices+1,vertices+1),int)
    
    for edge in edges:
        start, end, weight = edge
        adj_matrix[start][end] = weight 
    
    for row in adj_matrix:
        outputfile.writelines(f"{' '.join(map(str, row))}\n")
# input
openfile = open("./input1a_1.txt", "r")
readfile = openfile.readlines()

edges = []
for num in readfile[1::]:
    data = [int(i) for i in num.split()]
    edges.append(data)

# output
outputfile = open("./output1a_1.txt", "w")

vertices = int(readfile[0].split()[0])
createAdjacencyMatrix(vertices, edges)
