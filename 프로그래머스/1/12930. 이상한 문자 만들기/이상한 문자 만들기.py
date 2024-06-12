def solution(s):
    flag = 0
    c_list = list(s)
    for i, v in enumerate(c_list):
        if v == " ":
            flag = 0
            continue
            
        if flag % 2 == 0:
            c_list[i] = c_list[i].upper()
        else:
            c_list[i] = c_list[i].lower()
            
        flag += 1

    return "".join(c_list)
