#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string, vector<vector<int>> queries) {
    for (const auto& query : queries) {
        int s = query[0];
        int e = query[1];
        
        while (s < e) {
            swap(my_string[s], my_string[e]);
            s++;
            e--;
        }
    }
    
    return my_string;
}