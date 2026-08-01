#include <string>

using namespace std;

int solution(string my_string, string is_prefix) {
    if (is_prefix.length() > my_string.length()) {
        return 0;
    }
    
    if (my_string.substr(0, is_prefix.length()) == is_prefix) {
        return 1;
    }
    
    return 0;
}