def solution(A,B):
    sum = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        sum += A[i] * B[i]
    
    return sum
    
def solution2(A,B):
    results = []
    perms = permutations(B, len(B))
    for ar in perms:
        sum = 0
        for i in range(len(A)):
            sum += A[i] * ar[i]
        results.append(sum)
    
    return min(results)

def permutations(arr, r):
    result = []
    
    def helper(current, remaining):
        if len(current) == r:
            result.append(current)
            return
        
        for i in range(len(remaining)):
            helper(current + [remaining[i]], remaining[:i] + remaining[i+1:])
        
    helper([], arr)
    return result