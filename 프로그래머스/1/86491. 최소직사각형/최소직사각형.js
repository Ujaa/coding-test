function solution(sizes) {
    const mins = [], maxs = [];
    
    sizes.forEach((size) => {
        mins.push(Math.min(...size));
        maxs.push(Math.max(...size));
    });
    
    return Math.max(...mins) * Math.max(...maxs);
}