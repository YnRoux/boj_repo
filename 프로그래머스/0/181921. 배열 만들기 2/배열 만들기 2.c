#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool isValid(int num) {
    while (num > 0) {
        int digit = num % 10;
        if (digit != 0 && digit != 5) {
            return false;
        }
        num /= 10;
    }
    return true;
}

int* solution(int l, int r) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * 100);
    int count = 0;
    
    for (int i = l; i <= r; ++i) {
        if (isValid(i)) {
            answer[count++] = i;
        }
    }
    
    if (count == 0) {
        answer[0] = -1;
    }
    
    return answer;
}