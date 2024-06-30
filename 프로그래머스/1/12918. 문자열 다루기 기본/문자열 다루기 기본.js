function solution(s) {
    const len = s.split("").length;
    return (len === 4 || len === 6) && s.match(/\D/) === null;
}