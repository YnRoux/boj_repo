#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> rank, vector<bool> attendance) {
    vector<pair<int, int>> candidates;
    
    for (int i = 0; i < rank.size(); ++i) {
        if (attendance[i]) {
            candidates.push_back({rank[i], i});
        }
    }
    
    sort(candidates.begin(), candidates.end());
    
    int a = candidates[0].second;
    int b = candidates[1].second;
    int c = candidates[2].second;
    
    return 10000 * a + 100 * b + c;
}