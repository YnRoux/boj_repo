#include <string>
#include <vector>

using namespace std;

string solution(string my_string, vector<int> indices) {
    vector<bool> is_deleted(my_string.length(), false);
    for (int idx : indices) {
        is_deleted[idx] = true;
    }
    
    string answer = "";
    for (int i = 0; i < my_string.length(); i++) {
        if (!is_deleted[i]) {
            answer += my_string[i];
        }
    }
    return answer;
}