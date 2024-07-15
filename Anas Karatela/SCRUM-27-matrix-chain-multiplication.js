function matrixChainMulti(arr , i , j){
    // Here i and j are dimensions of the matrix
    if (i == j)
        return 0;
 
    let min = Number.MAX_VALUE;

    let k=0;
    for (k = i; k < j; k++) 
    {
        let count = matrixChainMulti(arr, i, k)
                    + matrixChainMulti(arr, k + 1, j)
                    + arr[i - 1] * arr[k] * arr[j];
 
        if (count < min)
            min = count;
    }

    return min;
}

// TESTCASE-1
let arr1=[10,30,5,60]
let n1=arr1.length
console.log(matrixChainMulti(arr1, 1, n1-1)) // Output: 4500

// TESTCASE-2
let arr2=[1,2,3,4,3]
let n2=arr2.length
console.log(matrixChainMulti(arr2, 1, n2-1)) // Output: 30
