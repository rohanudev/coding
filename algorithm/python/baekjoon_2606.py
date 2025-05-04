from collections import defaultdict

Computer = int(input())
net = int(input())

graph = defaultdict(list)

for i in range(net):
    a,b = map(int,(input().split()))
    graph[a].append(b)
    graph[b].append(a)

Visited = [False] * (Computer+1)

def dfs(node):
    Visited[node] = True
    for neighbor in graph[node]:
        if not Visited[neighbor]:
            dfs(neighbor)

dfs(1)

print(sum(Visited)-1) 