function solution(absolutes, signs) {
    return absolutes.reduce((acc, curr, i) => acc + getInt(curr, signs[i]) ,0)
}

function getInt(num, isPositive){
    return isPositive ? num : num * -1;
}