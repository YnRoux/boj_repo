#include <string>
#include <vector>

using namespace std;

int solution(vector<int> arr) {
    int count = 0;
    
    while (true) {
        vector<int> next_arr = arr;
        for (int i = 0; i < next_arr.size(); ++i) {
            if (next_arr[i] >= 50 && next_arr[i] % 2 == 0) {
                next_arr[i] /= 2;
            } else if (next_arr[i] < 50 && next_arr[i] % 2 != 0) {
                next_arr[i] = next_arr[i] * 2 + 1;
            }
        }
        
        if (arr == next_arr) {
            return count;
        }
        
        arr = next_arr;
        count++;
    }
}