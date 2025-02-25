function solution(n, left, right) {
    const arr = [];
    
    for (let x = left; x <= right; x++) {
        const a = Math.floor(x / n) + 1;
        const b = (x + 1) % n == 0 ? n : (x + 1) % n;
        arr.push(Math.max(a, b));
    }
    
    return arr
}