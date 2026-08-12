#include <string>
#include <vector>

using namespace std;

vector<int> solution(string myString) {
    vector<int> answer;
    int length = 0;
    
    for (char c : myString) {
        if (c == 'x') {
            answer.push_back(length);
            length = 0;
        } else {
            length++;
        }
    }
    answer.push_back(length);
    return answer;
}