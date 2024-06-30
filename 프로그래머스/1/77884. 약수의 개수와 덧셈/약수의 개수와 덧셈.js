function solution(left, right) {
    let sum = 0;
    for(let x = left; x <= right; x++){
        Math.sqrt(x) % 1 == 0 ? sum -= x : sum += x;
    }
    return sum;
}