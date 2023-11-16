from collections import defaultdict

# recursive dfs function
def dfs(graph, start):
    visited = set()
    path = []

    def dfs_recursive(node):
        nonlocal visited, path
        visited.add(node)
        path.append(node)

        for adjs in graph[node]:
            if adjs not in visited:
                dfs_recursive(adjs)

    dfs_recursive(start)
    return path

# input output
openfile = open("./input3_3.txt", "r")
readfile = openfile.readlines()
outputfile = open("./output3_3.txt", "w")
n, m = [int(i) for i in readfile[0].split()]
roads = [ [int(i) for i in p.split()] for p in readfile[1::]]

start = 1
graph = defaultdict(list)
for road in roads:
    u, v = road
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

dfs_path = dfs(graph, start)
# print(dfs_path)

outputfile.write(" ".join(map(str, dfs_path)))