function solution(s, n) {
    return [...s].map((c) => {
        if(c === " ") return c;
        return c.toUpperCase() === c ? getChangedChar(c, n, 65) : getChangedChar(c, n, 97);
    }).join("");
}

function getChangedChar(c, n, start){
    return String.fromCharCode((c.charCodeAt() - start + n) % 26 + start);
}