#include <iostream>
#include <string>
using namespace std;

string defangIPaddr(string address) {
    std::string defanged;
    for (char c : address) {
        if (c == '.') {
            defanged += "[.]";
        } else {
            defanged += c;
        }
    }
    return defanged;
}

int main() {
    string input = "1.1.1.1"; 
   string defangedAddress = defangIPaddr(input);
 cout << "Defanged IP address: " << defangedAddress << endl;
    return 0;
