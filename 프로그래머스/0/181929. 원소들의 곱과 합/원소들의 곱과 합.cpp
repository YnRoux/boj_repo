#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int mul = 1;
    int sum = 0;
    for (int num : num_list) {
        mul *= num;
        sum += num;
    }
    int sum_square = sum * sum;
    return (mul < sum_square) ? 1 : 0;
}