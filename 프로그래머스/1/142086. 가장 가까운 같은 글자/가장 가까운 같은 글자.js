function solution(s) {
    const dict = {};
    const answer = [];
    
    s.split("").forEach(
        (c, i) => {
            c in dict ? answer.push(i - dict[c]) :  answer.push(-1);
            dict[c] = i;
        }
    );
    
    return answer;
}