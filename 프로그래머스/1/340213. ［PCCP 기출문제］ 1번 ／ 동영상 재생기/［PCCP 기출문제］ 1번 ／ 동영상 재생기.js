function solution(video_len, pos, op_start, op_end, commands) {
    let current = getSeconds(pos);
    const videoLenSec = getSeconds(video_len);
    const opStartSec = getSeconds(op_start);
    const opEndSec = getSeconds(op_end);
    
    current = checkOpening(current, opStartSec, opEndSec)

    commands.forEach(command => {
        if (command === "next") {
            current = videoLenSec - current < 10 ? videoLenSec : current + 10
        } else if (command === "prev") {
            current = current < 10 ? 0 : current - 10
        }
        current = checkOpening(current, opStartSec, opEndSec)
    });
    
    return getTimeStr(current);
}

function checkOpening(current, start, end) {
    return current >= start && current <= end ? end : current
}

function getSeconds(str) {
    const [minutes, seconds] = str.split(":").map(val => parseInt(val))
    return minutes * 60 + seconds
}

function getTimeStr(sec){
    const minutes = Math.floor(sec / 60)
    const seconds = sec % 60
    
    return `${getPadding(minutes.toString())}:${getPadding(seconds.toString())}`
}

function getPadding(str) {
    return str.padStart(2, "0")
}