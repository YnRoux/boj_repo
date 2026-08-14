#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    int target_len = 1;
    
    while (target_len < arr.size()) {
        target_len *= 2;
    }
    
    arr.resize(target_len, 0);
    
    return arr;
}