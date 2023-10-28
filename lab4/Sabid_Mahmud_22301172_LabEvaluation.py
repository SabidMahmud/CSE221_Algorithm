from collections import deque

def bfs(graph, start):
    traversed = set()  
    queue = deque()   
    queue.append(start)
    traversed.add(start)
    
    while queue:
        node = queue.popleft()  
        print(node, end=" ")           
        
        for i, x in graph[node]:
            if i not in traversed:
                queue.append(i)
                traversed.add(i)

inp = {
    1:[(4,3), (1,3)],
    2:[(3, 2)],
    3:[(1, 4)],
    4:[],
    5:[]
}

start = 1
print("BFS Path Traversal:")
bfs(inp, start)

