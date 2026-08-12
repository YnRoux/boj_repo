#include <string>

using namespace std;

int solution(string myString, string pat) {
    for (char &c : myString) {
        if (c == 'A') {
            c = 'B';
        } else if (c == 'B') {
            c = 'A';
        }
    }
    
    if (myString.find(pat) != string::npos) {
        return 1;
    }
    
    return 0;
}