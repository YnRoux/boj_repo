#include <vector>
#include <unordered_set>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    unordered_set<int> visited;
    
    for (int num : arr) {
        if (answer.size() == k) break;
        
        if (visited.find(num) == visited.end()) {
            visited.insert(num);
            answer.push_back(num);
        }
    }
    
    while (answer.size() < k) {
        answer.push_back(-1);
    }    
    
    return answer;
}