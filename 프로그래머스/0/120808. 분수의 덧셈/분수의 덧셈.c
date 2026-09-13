#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int get_gcd(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int* solution(int numer1, int denom1, int numer2, int denom2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int numer = numer1 * denom2 + numer2 * denom1;
    int denom = denom1 * denom2;
    
    int gcd = get_gcd(numer, denom);
    
    int* answer = (int*)malloc(sizeof(int) * 2);
    answer[0] = numer / gcd;
    answer[1] = denom / gcd;
    
    return answer;
}