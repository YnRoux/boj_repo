#include <string>
#include <algorithm>

using namespace std;

string solution(string a, string b) {
    string result = "";
    int i = a.size() - 1;
    int j = b.size() - 1;
    int carry = 0;
    
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        
        if (i >= 0) {
            sum += a[i] - '0';
            i--;
        }
        if (j >= 0) {
            sum += b[j] - '0';
            j--;
        }
        
        carry = sum / 10;
        result.push_back((sum % 10) + '0');
    }
    
    reverse(result.begin(), result.end());
    
    return result;
}