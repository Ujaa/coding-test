function solution(numbers) {
    const nums = "0123456789";
    const regex = new RegExp(`[^${numbers.join("")}]`, "g");
    
    return nums.match(regex).reduce((acc, curr) => acc + parseInt(curr), 0);
}