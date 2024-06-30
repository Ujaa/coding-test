function solution(a, b) {
    return a.reduce((acc, num, index) => acc += num * b[index], 0);
}