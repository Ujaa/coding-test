class Solution:
    def isValid(self, s: str) -> bool:
        c_dic = {
            "{": "}", 
            "(": ")",
            "[": "]"
        }

        if len(s) % 2 != 0:
            return False
        
        stack = []

        try:
            for c in s:
                if c in c_dic.keys():
                    stack.append(c)
                    continue
                elif c in c_dic.values():
                    if c_dic[stack.pop()] != c:
                        return False
                else:
                    return False
        except:
            return False
        
        return True if len(stack) == 0 else False