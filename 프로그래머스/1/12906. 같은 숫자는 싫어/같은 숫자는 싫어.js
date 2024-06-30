function solution(arr){
    const answer = [];
    let last = null;
    
    arr.forEach(num => {
        if(num !== last) answer.push(num);
        last = num;
    })
    
    return answer;
}