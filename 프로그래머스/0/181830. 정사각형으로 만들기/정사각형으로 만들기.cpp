#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr) {
    int row = arr.size();
    int col = arr[0].size();
    
    if (row > col) {
        for (int i = 0; i < row; ++i) {
            arr[i].resize(row, 0);
        }
    }
    else if (col > row) {
        arr.resize(col, vector<int>(col, 0));
    }
    return arr;
}