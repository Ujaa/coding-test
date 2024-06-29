function solution(x) {
    return x % x.toString().split("").reduce((acc, curr) => acc + parseInt(curr), 0) == 0
}