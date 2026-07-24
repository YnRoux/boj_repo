#include <string>
#include <algorithm>

using namespace std;

int solution(int a, int b) {
    int ab = stoi(to_string(a) + to_string(b));
    int double_ab = 2 * a * b;
    return max(ab, double_ab);
}