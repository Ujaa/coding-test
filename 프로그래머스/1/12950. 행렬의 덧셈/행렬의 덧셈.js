function solution(arr1, arr2) {
    return arr1.map((arr, row) => {
        const result = [];
        for (let col = 0; col < arr.length; col++){
            result.push(arr[col] + arr2[row][col]);
        }
        return result;
    });
}