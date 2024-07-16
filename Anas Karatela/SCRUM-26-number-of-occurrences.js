function noOfOccurrences(arr,n,x){
    let count =0
    for(let i=0;i<n;i++){
        if(arr[i]===x){
            count++
        }
    }
    return count
}

// TESTCASE-1
let arr1=[1,1,2,2,2,2,3]
let n1= arr1.length
let x1= 2

console.log(noOfOccurrences(arr1,n1,x1)) // Output: 4

// TESTCASE-2
let arr2=[1,1,2,2,2,2,3,3,3]
let n2= arr2.length
let x2= 3

console.log(noOfOccurrences(arr2,n2,x2)) // Output: 3