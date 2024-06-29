# Intuition
문자열에서 대소문자 구분 없이 `p 혹은 P의 개수`와 `y 혹은 Y의 개수`가 같은지 판별한다.

# Approach
`정규 표현식`을 이용해 문자열에서 `p 혹은 P의 개수`와 `y 혹은 Y의 개수`를 세기로 했다.<br/>
`match` 함수를 이용해 문자열에서 조건을 만족하는 문자를 배열 형태로 받아 배열의 `length`가 같은지 계산한다.

> match 함수는 조건을 만족하는 문자가 없으면 `null`을 반환한다. 그래서 `null`일 경우 length 값 대신 0을 개수로 지정했다.

# Complexity
- Time complexity:
$$O(n)$$
- Space complexity:
$$O(1)$$

# Code
### 첫 문제풀이
```js
function solution(s){
    const pCount = s.match(/[pP]/gm) != null ? s.match(/[pP]/gm).length : 0;
    const yCount = s.match(/[yY]/gm) != null ? s.match(/[yY]/gm).length : 0;
    return pCount === yCount;
}
```
### 사람들의 해결방법 참고 후 수정
`||` 연산자를 사용하면 `null`일 때 삼항연산자로 0을 지정하지 않고 빈 배열을 반환한 것처럼 만들 수 있다. 
`||`은 왼쪽 피연산자가 true일 때 왼쪽 피연산자의 결과를 반환하고 왼쪽 피연산자가 false일 때 오른쪽 피연산자를 반환하기 때문이다.

```js
function solution(s){
    return (s.match(/p/igm) || []).length === (s.match(/y/igm) || []).length;
}
```
