function majorityElements(arr)
{
    let maxCount = 0;
    let index = Number.NEGATIVE_INFINITY;
    
    for(let i = 0; i < arr.length; i++){
        let count = 0;
        for(let j = 0; j < arr.length; j++){
            if (arr[i] == arr[j])
                count++;
        }

        if (count > maxCount){
            maxCount = count;
            index = i;
        }
    }
    if (maxCount > arr.length/ 2)
        console.log(arr[index]);
    else
        console.log("No Majority Element");
}

// TESTCASE-1
majorityElements([3,2,3]) // Output : 3

// TESTCASE-2
majorityElements([3,2,3,4]) // Output :No Majority Element