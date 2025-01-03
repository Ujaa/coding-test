def solution(s):
    converted = 0
    zero_count = 0
    
    while s != "1":
        str_len = len(s)
        current_zero_count = s.count("0")
        zero_count += current_zero_count
        s = format(str_len - current_zero_count, "b")
        converted += 1
        
    return [converted, zero_count]