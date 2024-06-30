function solution(price, money, count) {
    const requiredMoney = price * count * (count + 1) / 2 - money
    return requiredMoney > 0 ? requiredMoney : 0; 
}