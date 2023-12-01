# Task 1 B
from collections import deque, defaultdict

def topological_sort_bfs(n, prerequisites):
    in_degree = [0] * (n+1)
    graph = defaultdict(list)

    for prereq in prerequisites:
        graph[prereq[0]].append(prereq[1])
        in_degree[prereq[1]] += 1

    queue = deque()

    for course in range(1, n+1):
        if in_degree[course] == 0:
            queue.append(course)

    order = []
    while queue:
        current_course = queue.popleft()
        order.append(current_course)

        for neighbor in graph[current_course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order

#========input output===========
for i in range(1,4):
    openfile = open(f"./input1B_{i}.txt", "r")
    readfile = openfile.readlines()
    # print(readfile)
    n, m = [int(i) for i in readfile[0].split()]
    prereqs = readfile[1:]
    prerequisites = [list(map(int, line.split())) for line in prereqs]
    # print(n, m, prerequisites)
    order = topological_sort_bfs(n, prerequisites)
    # print(*order)
    outputfile = open(f"./output1B_{i}.txt", "w")
    if len(order) == n:
        [outputfile.write(str(x)+" ") for x in order]
    else:
        outputfile.write("IMPOSSIBLE")
