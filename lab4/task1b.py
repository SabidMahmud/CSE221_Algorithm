def createAdjList(vertaces, edges):
    adjList = {i: [] for i in range(0, vertaces+1)}

    for edge in edges:
        start, end, weight = edge
        adjList[start].append((end, weight))
    return adjList

def printAdjList(adjlist):
    for vertace, adjs in adjlist.items():
        outputfile.writelines(f"{vertace} : ")
        outputfile.writelines(' '.join([f"{i}" for i in adjs]))
        outputfile.writelines("\n")

# input-output
openfile = open("./input1a_1.txt", "r")
readfile = openfile.readlines()
outputfile = open("./output1b_1.txt", "w")

n, m = [int(i) for i in readfile[0].split()]

edges = []

for num in readfile[1:]:
    vertaceInfo = [int(i) for i in num.split()]
    edges.append(vertaceInfo)

adjList = createAdjList(n, edges)
printAdjList(adjList)