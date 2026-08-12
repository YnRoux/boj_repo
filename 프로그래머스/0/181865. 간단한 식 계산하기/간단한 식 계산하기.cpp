#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string binomial) {
    stringstream ss(binomial);
    int a, b;
    char op;
    
    ss >> a >> op >> b;
    
    if (op == '+') {
        return a + b;
    } else if (op == '-') {
        return a - b;
    } else if (op == '*') {
        return a * b;
    }
}