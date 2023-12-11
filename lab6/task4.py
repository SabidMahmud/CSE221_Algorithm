def building_graph(N, edges):
    graph_1 = [[] for i in range(N + 1)]
    for u, v, w in edges:
        graph_1[u].append((v, w))
        graph_1[v].append((u, w))
    return graph_1

def prim_minimum_spanning_tree(N, graph):
    visit = [False] * (N + 1)
    cost = [float("inf")] * (N + 1)
    cost[1] = 0
    total = 0
    for i in range(N):
        min_cost = float("inf")
        min_node = -1
        for node in range(1, N + 1):
            if not visit[node] and cost[node] < min_cost:
                min_cost = cost[node]
                min_node = node
        if min_node == -1:
            break
        visit[min_node] = True
        total += min_cost
        for next, nextcost in graph[min_node]:
            if not visit[next] and nextcost < cost[next]:
                cost[next] = nextcost
    return total




inputfile = open("./input4_2.txt", "r")
outputfile = open("./output4_2.txt", "w")
N,M = map(int, inputfile.readline().split())

edges = []

for i in range(M):
    u, v, w = map(int, inputfile.readline().split())
    edges.append((u, v, w))
graph = building_graph(N, edges)
min_cost = prim_minimum_spanning_tree(N, graph)
print(min_cost, file=outputfile)
inputfile.close()
outputfile.close()