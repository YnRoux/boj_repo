#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len) {
    int count[1000] = {0};
    
    for (size_t i = 0; i < array_len; ++i) {
        count [array[i]]++;
    }
    
    int max_count = 0;
    int mode = -1;
    bool is_duplicated = false;
    
    for (int i = 0; i < 1000; ++i) {
        if (count[i] > max_count) {
            max_count = count[i];
            mode = i;
            is_duplicated = false;
        } else if (count[i] == max_count && max_count > 0) {
            is_duplicated = true;
        }
    }
    
    return is_duplicated ? -1 : mode;
}