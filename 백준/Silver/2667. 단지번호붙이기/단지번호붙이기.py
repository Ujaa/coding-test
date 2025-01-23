from collections import deque

def bfs(start_x, start_y, visited):
    que = deque([(start_x, start_y)])
    visited[start_y][start_x] = 1
    house_count = 0

    while que:
      x, y = que.popleft()
      house_count += 1

      for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= next_x < count and 0 <= next_y < count and lines[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
          visited[next_y][next_x] = 1
          que.append((next_x, next_y))

    return house_count

def solution(count, lines):
  houses = []
  visit_count = 0
  visited = [[0] * count for _ in range(count)] # [[0] * count] * count x

  for y in range(count):
    for x in range(count):
      if lines[y][x] == 1 and visited[y][x] == 0:
        houses.append(bfs(x, y, visited))

  houses.sort()
  print(len(houses))
  for house in houses:
    print(house)

count = int(input())
lines = [list(map(int, input())) for _ in range(count)]

solution(count, lines)