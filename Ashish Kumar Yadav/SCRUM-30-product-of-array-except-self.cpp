#include<bits/stdc++.h>

using namespace std;

int pro(int arr[] , int n){
     int product = 1;
    for(int i = 0 ;i<n;i++){
        product = product*arr[i];
    }
    return product;
}

int main(){
    int aar[] = {1,2,3,4};
    int n = sizeof(aar)/sizeof(aar[0]);
    int p = pro( aar ,n);
    int ans[n];

 for(int i = 0 ;i<n;i++){
        ans[i] = p/aar[i];
    }
 for(int i = 0 ;i<n;i++){
       cout<<ans[i]<<" " ;
    }
    return 0;
}
