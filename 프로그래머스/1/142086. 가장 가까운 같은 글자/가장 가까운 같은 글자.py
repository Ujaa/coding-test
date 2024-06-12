def solution(s):
    arr = []
    c_dic = {}
    
    for i, x in enumerate(s):
        if x in c_dic:
            arr.append(i - c_dic[x])
        else:
            arr.append(-1)
        c_dic[x] = i
        
    return arr