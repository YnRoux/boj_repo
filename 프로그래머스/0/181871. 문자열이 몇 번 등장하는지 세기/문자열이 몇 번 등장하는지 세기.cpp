#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    int count = 0;
    int pos = myString.find(pat, 0);
    while (pos != string ::npos) {
        count ++;
        pos = myString.find(pat, pos + 1);
    }
    return count;
}