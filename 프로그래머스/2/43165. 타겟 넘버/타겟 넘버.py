def solution(numbers, target):
    def dfs(level, total):
        if level == len(numbers):
            return 1 if total == target else 0
                
        return dfs(level + 1, total + numbers[level]) + dfs(level + 1, total - numbers[level])
        
    return dfs(0, 0)