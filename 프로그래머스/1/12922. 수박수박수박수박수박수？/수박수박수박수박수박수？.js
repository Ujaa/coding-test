function solution(n) {
    let str = "수박".repeat(Math.floor(n/2));
    if(n % 2 !== 0) str += "수";
    return str;
}