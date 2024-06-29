function solution(a, b) {
    if(a === b) return a;
    return new Array(Math.abs(a - b) + 1).fill(0)
        .map((num, i) => i + Math.min(a, b))
        .reduce((acc, num) => acc + num, 0);
}