# Intuition
괄호의 짝을 찾아야 하기 때문에 dictionary를 이용해 매핑 테이블을 이용한다. 스택을 이용해 (, {, [ 문자를 쌓다가 ), }, ] 를 만나면 쌓여 있는 문자 중 가장 마지막 문자를 확인해 짝이 맞는지 확인한다.

# Approach
1. 매핑 테이블 생성
2. 문자열을 한 글자씩 살펴본다.
3. 만약 (, {, [ 중에 하나라면 스택에 쌓는다.
4. 만약 ), }, ] 중에 하나라면 스택에 요소가 존재하는지 확인하고 마지막 요소와 짝이 맞는지 확인하다. 짝이 맞지 않거나 스택에 요소가 존재하지 않으면 False를 return 한다.
5. 모든 문자열을 다 살펴본 뒤 스택에 남은 게 없다면 True를, 아니라면 False를 return한다.

# Complexity
- Time complexity:
$$O(n)$$
- Space complexity:
$$O(n)$$

# Code
```py
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
            else:
                if not stack or c_dic[stack.pop()] != c:
                    return False

        return len(stack) == 0
```
