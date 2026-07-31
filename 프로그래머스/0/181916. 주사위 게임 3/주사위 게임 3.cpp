#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solution(int a, int b, int c, int d) {
    vector<int> v = {a, b, c, d};
    sort(v.begin(), v.end());
    
    if (v[0] == v[3]) {
        return 1111 * v[0];
    }
    
    if (v[1] == v[3]) {
        int p = v[1];
        int q = v[0];
        return (10 * p + q) * (10 * p + q);
    }
    
    if (v[0] == v[2]) {
        int p = v[0];
        int q = v[3];
        return (10 * p + q) * (10 * p + q);
    }
    
    if (v[0] == v[1] && v[2] == v[3]) {
        int p = v[0];
        int q = v[2];
        return (p + q) * abs(p - q);
    }
    
    if (v[0] == v[1]) return v[2] * v[3];
    if (v[1] == v[2]) return v[0] * v[3];
    if (v[2] == v[3]) return v[0] * v[1];
    
    return v[0];
}