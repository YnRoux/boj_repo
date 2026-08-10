#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

int solution(string myString, string pat) {
    for (char &c : myString) {
        c = tolower(c);
    }
    for (char &c : pat) {
        c = tolower(c);
    }
    if (myString.find(pat) != string::npos) {
        return 1;
    }
    return 0;
}