#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer;
    
    for (const auto& query : queries) {
        int s = query[0];
        int e = query[1];
        int k = query[2];
        
        int min_val = 1000001;
        
        for (int i = s; i <= e; i++) {
            if (arr[i] > k && arr[i] < min_val) {
                min_val = arr[i];
            }
        }
        
        if (min_val == 1000001) {
            answer.push_back(-1);
        } else {
            answer.push_back(min_val);
        }
    }
    
    return answer;
}