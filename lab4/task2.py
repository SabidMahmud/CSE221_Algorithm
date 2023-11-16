from collections import deque, defaultdict

def bfs(graph, source):
    visited = set() 
    queue = deque([source]) 
    visited.add(source)
    
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(str(vertex))
        
        for adjs in graph[vertex]:
            if adjs not in visited:
                queue.append(adjs)
                visited.add(adjs)

    return ' '.join(result)


# input output
openfile = open("./input2_1.txt", "r")
readfile = openfile.readlines()
outputfile = open("./output2_1.txt", "w")
n, m = [int(i) for i in readfile[0].split()]
roads = [ [int(i) for i in p.split()] for p in readfile[1::]]

graph = defaultdict(list)
for road in roads:
    u, v = road
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

outputfile.write(bfs(graph, 1))
outputfile.write("\n")