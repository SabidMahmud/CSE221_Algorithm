from collections import defaultdict

def meeting_point(graph, N, s, t):
    alice_dist = [float('inf')] * (N + 1)
    bob_dist = [float('inf')] * (N + 1)
    alice_dist[s] = 0
    bob_dist[t] = 0
    alice_queue = [(0, s)]
    bob_queue = [(0, t)]
    while alice_queue:
        dist, node = alice_queue.pop(0)
        # print(dist, node)
        if dist > alice_dist[node]:
            continue

        for neighbor, weight in graph[node]:
            dist_1 = dist + weight
            if dist_1 < alice_dist[neighbor]:
                alice_dist[neighbor] = dist_1
                alice_queue.append((dist_1, neighbor))

    while bob_queue:
        dist, node = bob_queue.pop(0)
        # print("bob", dist, node)
        if dist > bob_dist[node]:
            continue
        for neighbor, weight in graph[node]:
            dist_1 = dist + weight
            if dist_1 < bob_dist[neighbor]:
                bob_dist[neighbor] = dist_1
                bob_queue.append((dist_1, neighbor))
   
    mini_time = float('inf')
    meet_node = -1
    for node in range(1, N + 1):
        if alice_dist[node] != float('inf') and bob_dist[node] != float('inf'):
            totaltime = max(alice_dist[node], bob_dist[node])
            if totaltime < mini_time:
                mini_time = totaltime
                meet_node = node
    return mini_time, meet_node

# input output
inputfile = open('./input2_1.txt', 'r')
outputfile = open('./output2_1.txt', 'w')
N, M = map(int, inputfile.readline().split())

graph = defaultdict(list)

for i in range(M):
    u, v, w = map(int, inputfile.readline().split())
    graph[u].append((v, w))
s, t = map(int, inputfile.readline().split())
min_time, meet_node = meeting_point(graph, N, s, t)
if meet_node != -1:
    outputfile.write("Time " + str(min_time) + "\n")
    outputfile.write("Node " + str(meet_node) + "\n")
else:
    outputfile.write("Impossible\n")
inputfile.close()
outputfile.close()