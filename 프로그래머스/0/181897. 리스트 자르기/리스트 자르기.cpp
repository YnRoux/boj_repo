#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, vector<int> slicer, vector<int> num_list) {
    int a = slicer[0];
    int b = slicer[1];
    int c = slicer[2];
    
    int start = 0;
    int end = num_list.size() - 1;
    int step = 1;
    
    if (n == 1) {
        end = b;
    } else if (n == 2) {
        start = a;
    } else if (n == 3) {
        start = a;
        end = b;
    } else if (n == 4) {
        start = a;
        end = b;
        step = c;
    }
    
    vector<int> answer;
    
    for (int i = start; i <= end; i+= step) {
        answer.push_back(num_list[i]);
    }
    
    return answer;
}