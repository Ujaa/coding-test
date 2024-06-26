# Intuition
palindrome인지 비교하려면 연결 리스트에 있는 값을 list로 저장한 뒤에 역순 슬라이싱을 이용해 비교하면 쉽게 구현할 수 있을거라 생각했다.

# Approach
1. 연결 리스트의 모든 노드를 순회하면서 value를 리스트에 저장
2. 순회가 끝난 후 reversed된 리스트와 원본 리스트를 비교해 palindrome인지 확인
   
# Complexity
- Time complexity: 모든 노드를 순회할 때 O(n)의 시간 복잡도를 가진다. 이후에 두 배열을 비교하는 작업도 O(n)의 시간 복잡도를 가진다. 최종 시간 복잡도는 O(n)이다.
$$O(n)$$

- Space complexity: 배열을 추가로 사용했기 때문이다.
$$O(n)$$


# Code
```py
# Definition for singly-linked list.

# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        return nums == nums[::-1]
```       
        
## 개선한 코드 1
데크 자료형을 이용해 양 옆의 요소를 동시에 확인하며 palindrome인지 확인하는 시간을 반으로 줄인다.

```py
# Definition for singly-linked list.

# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums : Deque = collections.deque() # 데크 사용

        if no head: # 예외를 확실히 처리
            return True

        node = head

        while node is not None: # 코드 가독성 향상
            nums.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
```         

## 개선한 코드 2
러너 기법을 이용한다. 2개의 포인터를 동시에 사용한다.

```py
# Definition for singly-linked list.

# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast: # fast가 있다는 것은 홀수개로 존재한다는 의미. 그럼 slow가 딱 가운데에 위치하고 있기 때문에 한 칸 앞으로 옮겨야 함.
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev
```

개선한 코드 1, 2는 파이썬 알고리즘 인터뷰 책에 나와있는 내용이다.
