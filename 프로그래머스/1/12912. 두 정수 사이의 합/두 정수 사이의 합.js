function solution(a, b) {
    if(a === b) return a;
    
    const min = Math.min(a, b);
    const max = Math.max(a, b);
    
    let sum = 0;
    
    for(let x = min; x <= max ; x++){
        sum += x;
    }
    
    return sum;
}