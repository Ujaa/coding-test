def solution(k, score):
    answer = []
    fame = []
    
    for s in score:
        fame.append(s)
        fame.sort()

        if len(fame) > k:
            fame = fame[-k:]
            
        answer.append(fame[0])
        
    return answer