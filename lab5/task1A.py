from collections import defaultdict

def dfs(course, graph, visited, result):
    visited[course] = 1
    
    for neighbor in graph[course]:
        if visited[neighbor] == 0:
            if not dfs(neighbor, graph, visited, result):
                return False
        elif visited[neighbor] == 1:
            return False
    
    visited[course] = 2
    result.append(course)    
    return True

def find_order(n, prerequisites):
    graph = defaultdict(list)
    for prerequisite in prerequisites:
        graph[prerequisite[0]].append(prerequisite[1])
    
    visited = [0] * (n + 1)
    result = []
    
    for course in range(1, n + 1):
        if visited[course] == 0:
            if not dfs(course, graph, visited, result):
                return []
    
    return result[::-1]

#========input output===========
for i in range(1,4):
    openfile = open(f"./input1A_{i}.txt", "r")
    readfile = openfile.readlines()
    # print(readfile)
    n, m = [int(i) for i in readfile[0].split()]
    prereqs = readfile[1:]
    prerequisites = [list(map(int, line.split())) for line in prereqs]
    # print(n, m, prerequisites)
    order = find_order(n, prerequisites)
    # print(*order)
    outputfile = open(f"./output1A_{i}.txt", "w")
    if len(order) == n:
        [outputfile.write(str(x)+" ") for x in order]
    else:
        outputfile.write("IMPOSSIBLE\n")
