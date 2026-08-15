#include <vector>
#include <unordered_set>

using namespace std;

vector<int> solution(vector<int> arr, vector<int> delete_list) {
    unordered_set<int> del_set(delete_list.begin(), delete_list.end());
    vector<int> answer;
    
    for (int num : arr) {
        if (del_set.find(num) == del_set.end()) {
            answer.push_back(num);
        }
    }
    return answer;
}