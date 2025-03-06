def solution(rows, columns, queries):
    answer = []

    arr = [[0] * columns for x in range(rows)]
    
    
    
    # 판 만들기
    count = 1
    for x in range(rows):
        for y in range(columns):
            arr[x][y] = count
            count += 1
            
    # 넣을 숫자 한바퀴 돌리고 다시 하나씩 넣기
    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        start = arr[x1][y1]
        
        min_num = start
        
        for i in range(x1, x2):
            arr[i][y1] = arr[i + 1][y1]
            if arr[i][y1] < min_num:
                min_num = arr[i][y1]
        
        for i in range(y1, y2):
            arr[x2][i] = arr[x2][i + 1]
            if arr[x2][i] < min_num:
                min_num = arr[x2][i]
            
        for i in range(x2, x1, -1):
            arr[i][y2] = arr[i - 1][y2]
            if arr[i][y2] < min_num:
                min_num = arr[i][y2]
            
        for i in range(y2, y1, -1):
            arr[x1][i] = arr[x1][i - 1]
            if arr[x1][i] < min_num:
                min_num = arr[x1][i]
        
        arr[x1][y1 + 1] = start
            
        answer.append(min_num)
    
    return answer