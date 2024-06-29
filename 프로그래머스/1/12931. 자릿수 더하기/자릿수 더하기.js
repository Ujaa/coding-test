function solution(n){
    return n.toString().split("").reduce((acc, curr) => acc + parseInt(curr), 0);
}