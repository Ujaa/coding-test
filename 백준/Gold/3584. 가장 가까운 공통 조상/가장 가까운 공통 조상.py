from collections import defaultdict

def solution(edges, node1, node2):
  graph = defaultdict(lambda: None)

  n1p = set()
  n2p = set()

  next_1 = None
  next_2 = None

  for edge in edges:
    p, c = edge
    graph[c] = p

  n1p.add(node1)
  n2p.add(node2)

  next_1 = graph[node1]
  next_2 = graph[node2]

  while next_1 != None or next_2 != None:
    if next_1 is not None:
      n1p.add(next_1)
      next_1 = graph[next_1]
    if next_2 is not None:
      n2p.add(next_2)
      next_2 = graph[next_2]
    
    intersection = n1p & n2p

    if len(intersection) > 0:
      return intersection.pop()

T = int(input())
cases = []
for _ in range(T):
  N = int(input())
  edges = [list(map(int, input().split())) for _ in range(N - 1)]
  node1, node2 = map(int, input().split())
  cases.append([edges, node1, node2])

for edges, node1, node2 in cases:
  print(solution(edges, node1, node2))