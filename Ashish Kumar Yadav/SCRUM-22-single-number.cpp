#include <iostream>
#include <vector>
using namespace std;

std::vector<int> findSingleNumbers(const vector<int>& nums) {
    int xorResult = 0;
    for (int num : nums) {
        xorResult ^= num;
    }

    int rightmostSetBit = xorResult & -xorResult;

    int num1 = 0, num2 = 0;
    for (int num : nums) {
        if (num & rightmostSetBit) {
            num1 ^= num;
        } else {
            num2 ^= num;
        }
    }

    return {num1, num2};
}

int main() {
    // Example usage
    vector<int> nums = {1, 2, 1, 3, 2, 5};
    vector<int> result = findSingleNumbers(nums);
    cout << "answer: [ " << result[0] << " , " << result[1] <<"]" << endl;

    return 0;
}
