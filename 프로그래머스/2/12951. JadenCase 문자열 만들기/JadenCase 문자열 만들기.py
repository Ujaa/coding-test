def solution(s):
    answer = ""
    is_before_blank = True

    for l in s:
        if l == " ":
            answer += l
            is_before_blank = True
        else:
            if is_before_blank:
                answer += l.upper()
            else:
                answer += l.lower()
            is_before_blank = False
    
    return answer