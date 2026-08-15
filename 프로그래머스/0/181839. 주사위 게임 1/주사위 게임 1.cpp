#include <cmath>

using namespace std;

int solution(int a, int b) {
    bool a_odd = (a % 2 != 0);
    bool b_odd = (b % 2 != 0);
    
    if (a_odd && b_odd) {
        return a * a + b * b;
    }
    else if (a_odd || b_odd) {
        return 2 * (a + b);
    }
    else {
        return abs(a - b);
    }
}