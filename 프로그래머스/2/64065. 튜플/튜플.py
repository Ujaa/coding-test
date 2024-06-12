def solution(s):
    answer, num_set, nums, num = [], [], [], ""
    
    for x in s[1:-1]:
        if x.isdigit():
            num += x
            continue
            
        if (x in [",", "}"] ) and num != "":
            nums.append(int(num))
            num = ""
            
        if x == "}":
            num_set.append(nums)
            nums = []
    
    num_set.sort(key=lambda x:len(x))
    
    for x in num_set:
        [answer.append(i) for i in x if i not in answer]
    
    return answer