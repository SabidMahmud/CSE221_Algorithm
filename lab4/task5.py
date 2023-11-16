from collections import defaultdict, deque

#find the sortest path
def shortest_path(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node == destination:
            return len(path) - 1, path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append((neighbor, path + [neighbor]))

    return -1, []

openfile = open("./input5_4.txt", "r")
readfile = openfile.readlines()
outputfile = open("./output5_4.txt", "w")
n, m, d = [int(i) for i in readfile[0].split()]
roads = [ [int(i) for i in p.split()] for p in readfile[1::]]

start = 1
graph = defaultdict(list)
for road in roads:
    u, v = road
    graph[u].append(v)
    graph[v].append(u)

time, path = shortest_path(graph, start, d)
outputfile.write(f"Time: {time}\n")
outputfile.write(f"Shortest Path: {' '.join(map(str, path))}")
