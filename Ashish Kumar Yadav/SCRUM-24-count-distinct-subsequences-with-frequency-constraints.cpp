#include <bits/stdc++.h>
using namespace std;

unordered_set<string> distinctSubsequences;

void subsequences(char s[], char op[], int i, int j) {
    if (s[i] == '\0') {
        op[j] = '\0';
        distinctSubsequences.insert(op);
        return;
    } else {
        op[j] = s[i];
        subsequences(s, op, i + 1, j + 1);
        subsequences(s, op, i + 1, j);
        return;
    }
}

int main() {
    char str[] = "ggg";
    int m = sizeof(str) / sizeof(char);
    int n = pow(2, m) + 1;
    char op[m + 1]; 
    subsequences(str, op, 0, 0);
    cout << distinctSubsequences.size(); 
    distinctSubsequences.clear();
    return 0;
}
