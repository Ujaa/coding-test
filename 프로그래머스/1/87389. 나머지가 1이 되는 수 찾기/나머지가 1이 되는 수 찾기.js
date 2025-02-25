function solution(n) {
    let x = 2;
    
    while (x < n) {
        if((n - 1) % x == 0) return x;
        x++;
    }
    
    return x;
}