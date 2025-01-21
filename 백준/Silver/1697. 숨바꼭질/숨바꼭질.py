from collections import deque

n, k = map(int, input().split())

def dfs(n, k, MAX=100001):
  arr = [0] * MAX
  que = deque([n])

  while que:
    loc = que.popleft()

    if loc == k:
      return arr[loc]

    for next in (loc+1, loc-1, loc*2):
      if 0<= next < MAX and arr[next] == 0:
        arr[next] = arr[loc] + 1
        que.append(next)

print(dfs(n, k))