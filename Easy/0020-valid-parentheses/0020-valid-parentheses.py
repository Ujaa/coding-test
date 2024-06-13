class Solution:
    def isValid(self, s: str) -> bool:
        c_dic = {
            "{": "}", 
            "(": ")",
            "[": "]"
        }

        stack = []

        for c in s:
            if c in c_dic.keys():
                stack.append(c)
                continue
            else:
                if not stack or c_dic[stack.pop()] != c:
                    return False

        
        return len(stack) == 0