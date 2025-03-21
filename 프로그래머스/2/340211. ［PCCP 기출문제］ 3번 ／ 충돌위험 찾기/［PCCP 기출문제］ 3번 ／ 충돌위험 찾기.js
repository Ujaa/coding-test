function solution(points, routes) {
    let answer = 0;
    const pointsObj = getPointsObj(points);
    let robots = [];
    
    routes = routes.map(route => route.reverse())
    
    routes.forEach((route, idx) => {
        const start = route.pop()
        const next = route.pop()
        robots.push([idx, start, next, pointsObj[start]])
    });
    
    const currPositions = {};
    robots.forEach(robot => {
        const [idx, start, next, current] = robot;
        const [currentX, currentY] = current;
        const key = getKey(currentX, currentY)
        currPositions[key] = (currPositions[key] || 0) + 1
    });
    answer += Object.values(currPositions).filter(count => count >= 2).length
    
    while (robots.length > 0) {
        const newRobots = [];
        const positions = {};
    
        robots.forEach(robot => {
            const [idx, start, next, current] = robot;
            const [currentX, currentY] = current;
            const [moveX, moveY] = getNextMove(current, pointsObj[next]);

            const nextX = currentX + moveX;
            const nextY = currentY + moveY;
            
            const key = getKey(nextX, nextY)
            positions[key] = (positions[key] || 0) + 1
            
            if (nextX == pointsObj[next][0] && nextY == pointsObj[next][1]){
                if (routes[idx].length > 0) {
                    const newNext = routes[idx].pop()
                    newRobots.push([idx, next, newNext, [nextX, nextY]]) 
                }
            }else {
                newRobots.push([idx, start, next, [nextX, nextY]]) 
            }
            
        });
       
        answer += Object.values(positions).filter(count => count >= 2).length
        robots = newRobots
    }
    return answer;
}

function getPointsObj(points) {
    const obj = {};
    
    points.forEach((point, index) => {
        const [x, y] = point
        obj[index + 1] = point
    })
    
    return obj
}

// x = 수직, y = 수평, [x, y]

function getNextMove(start, end) {
    const [startX, startY] = start;
    const [endX, endY] = end;
    
    if (startX < endX) return [1, 0]
    if (startX > endX) return [-1, 0]
    if (startY < endY) return [0, 1]
    if (startY > endY) return [0, -1]
    return [0, 0]
}

function getKey(x, y) {
    return `${x}_${y}`
}
          