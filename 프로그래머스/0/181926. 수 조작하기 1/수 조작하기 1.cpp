#include <string>
#include <vector>

using namespace std;

int solution(int n, string control) {
    for (char ch : control) {
        if (ch == 'w') {
            n += 1;
        } else if (ch == 's') {
            n -= 1;
        } else if (ch == 'd') {
            n += 10;
        } else if (ch == 'a') {
            n -= 10;
        }
    }
    return n;
}