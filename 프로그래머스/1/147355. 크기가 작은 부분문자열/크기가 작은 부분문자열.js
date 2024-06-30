function solution(t, p) {
    let answer = 0;
    for(let x = 0; x <= t.length - p.length; x++){
        if(t.substring(x, x + p.length) <= p) answer++;
    }
    return answer;
}