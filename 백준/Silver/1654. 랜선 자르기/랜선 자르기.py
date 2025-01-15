k, n = map(int, input().split())
nums = [int(input()) for x in range(k)]
start, end = 1, max(nums)

while start <= end:
  mid = (start + end) // 2
  lines = 0
  
  for i in nums:
    lines += i // mid
    
  if lines >= n:
    start = mid + 1
  else:
    end = mid - 1

print(end)