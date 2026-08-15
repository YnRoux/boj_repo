#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> board, int k) {
    int answer = 0;
    int row = board.size();
    int col = board[0].size();
    
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col && j <= k - i; ++j) {
            answer += board[i][j];
        }
    }
    return answer;
}