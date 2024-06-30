function solution(d, budget) {
    const sortedArr = d.sort((a,b) => b - a);
    console.log(sortedArr);
    let count = 0;
    while(budget > 0 && sortedArr.length > 0){
        const budg = sortedArr.pop();
        if(budget - budg < 0) break;
        budget -= budg;
        count++;
    }
    return count;
}