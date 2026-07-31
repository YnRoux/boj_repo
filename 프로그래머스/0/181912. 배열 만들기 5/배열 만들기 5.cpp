#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> intStrs, int k, int s, int l) {
    vector<int> answer;
    for (const string& str : intStrs) {
        string sub = str.substr(s, l);
        int num = stoi(sub);
        if (num > k) {
            answer.push_back(num);
        }
    }
    return answer;
}