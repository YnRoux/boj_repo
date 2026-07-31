#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string is_suffix) {
    if (my_string.length() < is_suffix.length()) {
        return 0;
    }
    
    int startIndex = my_string.length() - is_suffix.length();
    string suffix = my_string.substr(startIndex);
    
    if (suffix == is_suffix) {
        return 1;
    } else {
        return 0;
    }
}