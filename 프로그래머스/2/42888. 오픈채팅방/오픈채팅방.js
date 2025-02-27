function solution(records) {
    const answer = [];
    const names = {};
    
    const enterStr = "님이 들어왔습니다.";
    const leaveStr = "님이 나갔습니다.";
    
    for(let record of records) {
        const [command, uid, nickname] = record.split(" ");
        if(names[uid] == undefined) names[uid] = nickname;
        if(command == "Change") names[uid] = nickname;
        if(command == "Enter") {
            answer.push([uid, enterStr]);
            if(names[uid]) names[uid] = nickname;
        }
        if(command == "Leave") answer.push([uid, leaveStr])
    }
    
    return answer.map(el => {
        const [uid, str] = el;
        return `${names[uid]}${str}`
    })
}

