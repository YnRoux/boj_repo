#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer(numbers.size());
    
    transform(numbers.begin(), numbers.end(), answer.begin(), [](int n) {
        return n * 2;
    });
    
    return answer;
}