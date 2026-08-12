#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<bool> flag) {
    vector<int> X;
    
    for (int i = 0; i < arr.size(); ++i) {
        if (flag[i]) {
            int count = arr[i] * 2;
            for (int j = 0; j < count; ++j) {
                X.push_back(arr[i]);
            }
        } else {
            int count = arr[i];
            for (int j = 0; j < count; ++j) {
                X.pop_back();
            }
        }
    }
    
    return X;
}