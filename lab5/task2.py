from collections import defaultdict, deque

def lex_smallest_order(n, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for prereq in prerequisites:
        graph[prereq[0]].append(prereq[1])
        in_degree[prereq[1]] += 1

    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    result = []

    while queue:
        current_course = queue.popleft()
        result.append(current_course)

        for neighbor in graph[current_course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


#========input output===========
for i in range(1,4):
    openfile = open(f"./input2_{i}.txt", "r")
    readfile = openfile.readlines()
    # print(readfile)
    n, m = [int(i) for i in readfile[0].split()]
    prereqs = readfile[1:]
    prerequisites = [list(map(int, line.split())) for line in prereqs]
    # print(n, m, prerequisites)
    order = lex_smallest_order(n, prerequisites)
    # print(*order)
    outputfile = open(f"./output2_{i}.txt", "w")
    if len(order) == n:
        [outputfile.write(str(x)+" ") for x in order]
    else:
        outputfile.write("IMPOSSIBLE\n")
