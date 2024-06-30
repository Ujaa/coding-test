function solution(s) {
    const arr = s.split("");
    const mid = Math.floor(arr.length/2);
    return arr.length % 2 === 0 ? 
        arr.slice(mid - 1, mid + 1).join("") : 
        arr.slice(mid, mid + 1).join("");
}