#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) {
    char str_ab[32];
    
    sprintf(str_ab, "%d%d", a, b);
    int ab = atoi(str_ab);
    int ab2 = 2 * a * b;
    
    return (ab >= ab2) ? ab : ab2;
}