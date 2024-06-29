function solution(s){
    const pCount = s.match(/[pP]/gm) != null ? s.match(/[pP]/gm).length : 0;
    const yCount = s.match(/[yY]/gm) != null ? s.match(/[yY]/gm).length : 0;
    return pCount === yCount;
}