def solution(N_count, N, M_count, M):
  for x in M:
    if x in N:
      print(1)
    else:
      print(0)

T = int(input())
for x in range(T):
  N_count = int(input())
  N = set(map(int, input().split()))
  M_count = int(input())
  M = map(int, input().split())

  solution(N_count, N, M_count, M)