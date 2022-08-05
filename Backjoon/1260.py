import sys
from collections import deque
input = lambda : sys.stdin.readline()

n,m,start=map(int,input().split()) # We input the data.
visited=[False]*(n+1) # We set visited to False.

graph=[[] for _ in range(n+1)] # Mapping the graph.

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# If it has more than one vertex that we can visit, we need to visit the smaller vertex one first.
for i in range(len(graph)):
    graph[i].sort() # We sorted.

def dfs(start):
    print(start, end=' ')
    visited[start]=True # The starting point should be True
    for i in graph[start]: # Since the starting point, we start to search inside the graph.
        if not visited[i]: # For every section that we didn't visit, we use recursion(dfs).
            dfs(i)
            visited[i]=True # Now we set as True.

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
dfs(start)
visited=[False]*(n+1)
print()
bfs(start)
