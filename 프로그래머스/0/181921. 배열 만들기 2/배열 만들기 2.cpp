#include <string>
#include <vector>

using namespace std;

vector<int> solution(int l, int r) {
    vector<int> answer;
    
    for (int i = l; i <= r; i++) {
        string num_str = to_string(i);
        bool is_valid = true;
        
        for (char ch : num_str) {
            if (ch != '0' && ch != '5') {
                is_valid = false;
                break;
            }
        }
        
        if (is_valid) {
            answer.push_back(i);
        }
    }
    
    if (answer.empty()) {
        answer.push_back(-1);
    }
    
    return answer;
}