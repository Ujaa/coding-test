function solution(begin, target, words) {
    const info = {};
    
    function getExceptWord(splitted, index) {
        return splitted.slice(0, index - 1).concat("_",...splitted.slice(index)).join("");
    }
    
    for(let word of words) {
        const splited = word.split("");
        for(let x = 1; x <= splited.length; x++) {
            const key = getExceptWord(splited, x);
            if(!info[key]) info[key] = [];
            info[key].push(word)
        }
    }
    
    let answers = [];
    function dfs(word, level = 0, visited = new Set()) {
        if(word == target) answers.push(level);
        if(visited.has(word) || level == words.length - 1) return visited;
        
        visited.add(word);
        const splitted = word.split("");
            
        for(let x = 1; x <= splitted.length; x++) {
            const key = getExceptWord(splitted, x);
            if(!info[key]) continue;
            info[key].forEach(next => {
                if(!visited[next]) {
                    visited = dfs(next, level + 1, visited);
                }
            })
        }
        
        return visited;
    }

    dfs(begin);
    
    return answers.length == 0 ? 0 : Math.min(...answers);
}