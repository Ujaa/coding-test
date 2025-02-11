const getWeekDays = (timelogs, startday) => {
    const result = Array.from({ length: timelogs.length }, () => []);

    let i = 0;
    while (i < 7) {
        const day = ((startday - 1 + i) % 7) + 1;
        if (1 <= day && day <= 5) {
            for (let j = 0; j < timelogs.length; j++) {
                result[j].push(timelogs[j][i]);
            }
        }
        i += 1;
    }

    return result;
};

const addMinutes = (time, minutes) => {
    const hour = Math.floor(time / 100);
    let min = time % 100;
    min += minutes;
    if (min >= 60) {
        return (hour + 1) * 100 + (min - 60);
    }
    return hour * 100 + min;
}

function solution(schedules, timelogs, startday) {
    const weekdays = getWeekDays(timelogs, startday);
    return weekdays.filter((w, i) =>
        w.every((d) => d <= addMinutes(schedules[i], 10))
    ).length;
}