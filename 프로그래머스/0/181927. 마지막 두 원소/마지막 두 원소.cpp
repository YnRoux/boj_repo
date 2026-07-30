#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    int n = num_list.size();
    
    int last = num_list[n-1];
    int prev = num_list[n-2];
    
    if (last > prev) {
        num_list.push_back(last - prev);
    } else {
        num_list.push_back(last * 2);
    }
    return num_list;
}