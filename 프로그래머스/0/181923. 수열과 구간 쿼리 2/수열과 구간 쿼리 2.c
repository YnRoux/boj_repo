#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
// queries_rows는 2차원 배열 queries의 행 길이, queries_cols는 2차원 배열 queries의 열 길이입니다.
int* solution(int arr[], size_t arr_len, int** queries, size_t queries_rows, size_t queries_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * queries_rows);
    
    for (size_t q = 0; q < queries_rows; ++q) {
        int s = queries[q][0];
        int e = queries[q][1];
        int k = queries[q][2];
        
        int min_val = -1;
        
        for (int i = s; i <= e; ++i) {
            if (arr[i] > k) {
                if (min_val == -1 || arr[i] < min_val) {
                    min_val = arr[i];
                }
            }
        }
        
        answer[q] = min_val;
    }
    
    return answer;
}