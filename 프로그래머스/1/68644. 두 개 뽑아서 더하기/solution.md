# Intuition

서로 다른 인덱스에 있는 두 수를 뽑아야 하기 때문에 이중 for문으로 요소를 겹치지 않게 뽑는다. 그리고 만들 수 있는 수에 중복이 없기 때문에 set 자료형을 이용한다.

# Approach

1. 이중 for문으로 numbers 배열에서 겹치지 않는 2개의 요소를 가져온다.
2. 두 요소를 더한 값을 집합에 추가한다.
3. for문을 모두 돈 이후에 집합을 리스트로 바꾼 후 오름차순으로 정렬한다.

# Complexity

- Time complexity:
  $$O(n^2*logn)$$
- Space complexity:
  $$O(n^2)$$

# Code

```py
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for l in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[l])
    return sorted(list(answer))
```
