#include <string>
#include <vector>

using namespace std;

string solution(string code) {
    string ret = "";
    int mode = 0;
    for (int idx = 0; idx < code.length(); idx++) {
        if (code[idx] == '1') {
            mode = 1 - mode;
        }
        else {
            if (mode == 0 && (idx & 1) == 0) {
                ret += code[idx];
            } else if (mode == 1 && (idx & 1) == 1) {
                ret += code[idx];
            }
        }
    }
    return ret.empty() ? "EMPTY" : ret;
}