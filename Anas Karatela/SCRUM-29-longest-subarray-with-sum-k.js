function longestSubArr(arr,k){
    let n=arr.length
    let maxL= 0

    for(let i=0;i<n;i++){
        let sum=0
        
        if(maxL== n-i)
             break;

        for(let j=i;j<n;j++){
            sum+=arr[j]

            if(sum==k){
                maxL=Math.max(maxL,j-i+1)
            }
        }
    }
    return maxL
}

// TESTCASE-1
console.log(longestSubArr([10, 5, 2, 7, 1, 9],15)) // Output: 4

// TESTCASE-2
console.log(longestSubArr([1, 4, 45, 6, 0, 19],15)) // Output: 0