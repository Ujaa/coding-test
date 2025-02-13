function solution(str1, str2) {
    const str1Set = getSub(str1);
    const str2Set = getSub(str2);
    
    const intersect = {};
    const union = Object.assign({}, str2Set);

    for(const x in str1Set) {
        if(str2Set[x]) {
            intersect[x] = str1Set[x] > str2Set[x] ? str2Set[x] : str1Set[x];
            union[x] = str1Set[x] > str2Set[x] ? str1Set[x] : str2Set[x];
        }else{
            union[x] = str1Set[x]
        }
    }
    const intersectCount = sumOfVal(intersect);
    const unionCount = sumOfVal(union);
    
    if(unionCount == 0 && unionCount == 0) return 1 * 65536;
    return Math.floor(intersectCount / unionCount * 65536);
}

function sumOfVal(dic){
    return Object.values(dic).reduce((accum, val) => accum += val, 0);
}

function getSub(str){
    const result = {};
    const pattern = /^[a-zA-Z]*$/;
    
    for(let x = 0; x < str.length - 1; x++) {
        const sub = str.slice(x, x + 2).toLowerCase();
        if(pattern.test(sub)) {
            if(!result[sub]) result[sub] = 0;
            result[sub]++;
        }
    }
    
    return result;
}