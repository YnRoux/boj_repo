#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> picture, int k) {
    vector<string> answer;
    
    for (const string& row : picture) {
        string expanded_row = "";
        for (char ch : row) {
            expanded_row += string(k, ch);
        }
        
        for (int i = 0; i < k; ++i) {
            answer.push_back(expanded_row);
        }
    }
    
    return answer;
}