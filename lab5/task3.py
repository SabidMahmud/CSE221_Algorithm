from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def dfs(graph, u, visited, stack):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited, stack)
    stack.append(u)

def transpose_graph(graph):
    transposed = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def dfs2(graph, u, visited, component):
    visited[u] = True
    component.append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs2(graph, v, visited, component)

def find_sccomponents(graph, n):
    visited = {u: False for u in range(1, n + 1)}
    stack = []
    for u in graph:
        if not visited[u]:
            dfs(graph, u, visited, stack)

    transposed = transpose_graph(graph)
    visited = {u: False for u in range(1, n + 1)}
    components = []

    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs2(transposed, u, visited, component)
            components.append(component)

    return components



inpt = open("./input3_1.txt", "r")
readfile = inpt.readlines()

N, M = map(int, readfile[0].split())

graph = defaultdict(list)
for i in range(1, M + 1):
    u, v = map(int, readfile[i].split())
    add_edge(graph, u, v)


visited = {u: False for u in range(1, N + 1)}
for u in range(1, N + 1):
    if not visited[u]:
        add_edge(graph, u, u)
        dfs(graph, u, visited, [])


components = find_sccomponents(graph, N)

outputfile = open("./output3_1.txt", "w")
for component in components:
    outputfile.write(' '.join(map(str, component)) + '\n')

inpt.close()
outputfile.close()