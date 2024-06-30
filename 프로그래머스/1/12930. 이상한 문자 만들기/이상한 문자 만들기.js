function solution(s) {
    let answer = "";
    s.split("").reduce((last, c, i) => {
        if(c === " "){
            answer += c;
        }else if(last === " ") {
            answer += c.toUpperCase();
        }else if(last.toUpperCase() === last){
            answer += c.toLowerCase();
        }else if(last.toLowerCase() === last){
            answer += c.toUpperCase();
        }
        return answer.slice(-1);
            
    }, " ");
    return answer;
}