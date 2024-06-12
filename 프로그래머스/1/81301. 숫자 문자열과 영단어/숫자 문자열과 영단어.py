def solution(s): 
    answer = ""
    text = ""
    
    num_dic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    for x in s:
        print(x)
        if x.isdigit():
            answer += x
        else:
            text += x
            if text in num_dic:
                answer += str(num_dic[text])
                text = ""
                
            
    return int(answer)