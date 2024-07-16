function partitionSubset(arr){
    let sum = arr.reduce((a, b) => a + b, 0);
    
    if (sum % 2 !== 0) {
        return false
    }
    
    let half = sum / 2
    let dp = [];
    
    dp[0] = true;
    
    for (let i = 0; i < arr.length; ++ i) {
        let array = arr[i];
        for (let i = half; i >= array; -- i) {
            dp[i] = dp[i] || dp[i - array];
        }
    }
    
    return dp[half] || false;
}

// TESTCASE-1
console.log(partitionSubset([1,5,11,5])) // Output: true

// TESTCASE-2
console.log(partitionSubset([1,2,3,7])) // Output: false