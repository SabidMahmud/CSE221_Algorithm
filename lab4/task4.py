from collections import defaultdict

def has_cycle(graph, node, visited, stack):
    visited[node] = True
    stack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, stack):
                return True
        elif stack[neighbor]:
            return True

    stack[node] = False
    return False

def contains_cycle(graph, N):
    visited = [False] * (N + 1)
    stack = [False] * (N + 1)

    for node in range(1, N + 1):
        if not visited[node]:
            if has_cycle(graph, node, visited, stack):
                return True
    
    return False

# input-output
openfile = open("./input4_2.txt", "r")
readfile = openfile.readlines()
outputfile = open("./output4_2.txt", "w")
n, m = [int(i) for i in readfile[0].split()]
roads = [ [int(i) for i in p.split()] for p in readfile[1::]]

start = 1
graph = defaultdict(list)
for road in roads:
    u, v = road
    graph[u].append(v)

cycle = contains_cycle(graph, n)
if cycle:
    # print("YES")
    outputfile.write("YES\n")

else:
    # print("NO")
    outputfile.write("NO\n")