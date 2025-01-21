from collections import deque

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, start):
  visited = set()
  stack = [start]

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      print(node, end=" ")
      stack.extend(graph[node])

def bfs(graph, start):
  visited = set()
  queue = deque([start])

  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      print(node, end=" ")
      queue.extend(graph[node])

for key, value in graph.items():
  value.sort(reverse=True)

dfs(graph, v)
print()

for key, value in graph.items():
  value.sort()

bfs(graph, v)