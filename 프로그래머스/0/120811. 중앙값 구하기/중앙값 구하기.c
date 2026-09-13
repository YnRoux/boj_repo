#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int num1 = *(const int *)a;
    int num2 = *(const int *)b;
    
    if (num1 < num2) return -1;
    if (num1 > num2) return 1;
    return 0;
}

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len) {
    qsort(array, array_len, sizeof(int), compare);
    
    return array[array_len / 2];
}