#include <numeric>

using namespace std;

int solution(int n) {
    return n / std::gcd(6, n);
}