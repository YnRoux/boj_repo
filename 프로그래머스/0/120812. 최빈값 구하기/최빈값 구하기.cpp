#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<int> array) {
    unordered_map<int, int> counts;
    for (int num : array) {
        counts[num]++;
    }
    
    int max_count = 0;
    int mode = -1;
    bool is_duplicated = false;
    
    for (const auto& [num, count] : counts) {
        if (count > max_count) {
            max_count = count;
            mode = num;
            is_duplicated = false;
        } else if (count == max_count) {
            is_duplicated = true;
        }
    }
    
    return is_duplicated ? -1 : mode;
}