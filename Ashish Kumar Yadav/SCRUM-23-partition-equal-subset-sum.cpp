#include <iostream>
#include <vector>


using namespace std;

bool canPartition(vector<int>& nums) {
    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }

    if (totalSum % 2 != 0) {
        return false;
    }

    int targetSum = totalSum / 2;
   vector<bool> dp(targetSum + 1, false);
    dp[0] = true;

    for (int num : nums) {
        for (int i = targetSum; i >= num; --i) {
            dp[i] = dp[i] || dp[i - num];
        }
    }

    return dp[targetSum];
}

int main() {
    vector<int> nums = {1, 5, 11, 5};
    bool result = canPartition(nums);
    cout << (result ? "true" : "false") << endl;

    return 0;
}
