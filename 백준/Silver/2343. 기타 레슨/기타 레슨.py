n, m = map(int, input().split())
lecs = list(map(int, input().split()))

start = max(lecs)
end = sum(lecs)

answer = -1

while start <= end:
  mid = (start + end) // 2
  
  total = 0
  count = 1
  for lec in lecs:
    if total + lec > mid:
      count += 1
      total = 0
    total += lec
  
  if count <= m:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)