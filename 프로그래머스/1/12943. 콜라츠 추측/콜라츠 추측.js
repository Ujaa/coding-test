function solution(num) {
    let step = 0;
    while(num !== 1 && step < 500){
        num % 2 === 0 ? num = num / 2: num = num * 3 + 1;
        step++;
    }
    return num !== 1 ? -1 : step;
}