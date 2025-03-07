from collections import deque

def solution(maps):
    height = len(maps)
    width = len(maps[0])
    
    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
    ]
                
    queue = deque([[0,0]])

    while queue:
        x, y = queue.popleft()
        current = maps[x][y]

        if x == height - 1 and y == width - 1:
            
            return current
        
        for dx, dy in directions:
            next_x = dx + x
            next_y = dy + y
            
            if next_x >= 0 and next_x < height and next_y >= 0 and next_y < width and maps[next_x][next_y] == 1:
                queue.append([next_x, next_y])
                maps[next_x][next_y] = current + 1
    
    return -1
