#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int odd_num = 0;
    int even_num = 0;
    
    for (size_t i = 0; i < num_list_len; ++i) {
        if (num_list[i] % 2 != 0) {
            odd_num = odd_num * 10 + num_list[i];
        } else {
            even_num = even_num * 10 + num_list[i];
        }
    }
    
    return odd_num + even_num;
}