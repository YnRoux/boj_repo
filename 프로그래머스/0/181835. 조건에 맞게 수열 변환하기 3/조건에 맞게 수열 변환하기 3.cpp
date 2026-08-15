#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    if (k % 2 != 0) {
        for (int &x : arr) {
            x *= k;
        }
    } else {
        for (int &x : arr) {
            x += k;
        }
    }
    return arr;
}