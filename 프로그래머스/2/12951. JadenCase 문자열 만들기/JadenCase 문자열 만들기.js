function solution(s) {
    const arr = s.split("");
    return arr.map((c,i) => i === 0 || (i !== 0 && arr[i-1] === " ") ? 
                   c.toUpperCase() : c.toLowerCase()).join("");
}