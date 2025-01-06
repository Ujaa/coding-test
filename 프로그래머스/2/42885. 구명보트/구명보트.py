def solution(people, limit):
    if len(people) == 1:
        return 1
    
    people.sort(reverse=True)
    
    answer = 0
    
    start = 0
    end = len(people) - 1
    
    while start <= end:
        if start == end:
            answer += 1
            start += 1
        elif people[start] + people[end] <= limit:
                answer += 1
                start += 1
                end -= 1
        else:
            answer += 1
            start += 1        
    
    return answer