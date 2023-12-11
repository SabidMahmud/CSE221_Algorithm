from collections import defaultdict

def dijkstra(graph, source, N):
    distance = [float('inf')] * (N + 1)
    distance[source] = 0
    K = [(0, source)]
    while K:
        dist, node = K.pop(0)
        if dist > distance[node]:
            continue
        for neighbor, weight in graph[node]:
            dist_1 = dist + weight
            if dist_1 < distance[neighbor]:
                distance[neighbor] = dist_1
                K.append((dist_1, neighbor))
    return distance[1:]

inputfile = open('./input1.txt', 'r')
outfile = open('./output1.txt', 'w')
readfile = inputfile.readline()
N, M = map(int, readfile.split())
graph = defaultdict(list)
for i in range(M):
    u, v, w = map(int, inputfile.readline().split())
    graph[u].append((v, w))
source = int(inputfile.readline())
distance = dijkstra(graph, source, N)
for d in distance:
    outfile.write(str(d) + " ")
inputfile.close()
outfile.close()