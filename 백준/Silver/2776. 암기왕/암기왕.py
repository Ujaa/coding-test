def find(list, num):
  start = 0
  end = len(list) - 1

  while start <= end:
    mid = (start + end) // 2
    mid_num = list[mid]
    if mid_num == num:
      return 1
    elif mid_num < num:
      start = mid + 1
    else:
      end = mid - 1

  return 0

t = int(input())

for _ in range(t):
  n = int(input())
  n_num = list(map(int, input().split()))
  n_num.sort()

  m = int(input())
  m_num = list(map(int, input().split()))

  for num in m_num:
    print(find(n_num, num))