#include <string>
#include <vector>

using namespace std;

string solution(string myString, string pat) {
    int last_idx = myString.rfind(pat);
    return myString.substr(0, last_idx + pat.length());
}