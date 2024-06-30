function solution(s) {
    let answer = "";
    let numStr = "";
    
    const numDic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    s.split("").forEach((w) => {
        if(!isNaN(w)){
            if(numStr !== "") answer += numDic[numStr];
            answer += w;
            numStr = "";
        }else{
            numStr += w;
            if(numStr in numDic) {
                answer += numDic[numStr];
                numStr = "";
            }
            
        }
    });
    
    if(numStr !== "") answer += numDic[numStr];
    
    return parseInt(answer);
}