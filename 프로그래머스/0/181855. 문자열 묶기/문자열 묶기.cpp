#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<string> strArr) {
    vector<int> lenCount(31, 0);
    
    for (const string& str : strArr) {
        lenCount[str.length()]++;
    }
    
    return *max_element(lenCount.begin(), lenCount.end());
}