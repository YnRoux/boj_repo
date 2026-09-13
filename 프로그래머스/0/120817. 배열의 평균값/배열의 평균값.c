#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
double solution(int numbers[], size_t numbers_len) {
    long long sum = 0;
    
    for (size_t i = 0; i < numbers_len; ++i) {
        sum += numbers[i];
    }
    
    return (double)sum / numbers_len;
}