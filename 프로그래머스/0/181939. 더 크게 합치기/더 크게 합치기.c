#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) {
    char str_ab[32];
    char str_ba[32];
    
    sprintf(str_ab, "%d%d", a, b);
    sprintf(str_ba, "%d%d", b, a);
    
    int ab = atoi(str_ab);
    int ba = atoi(str_ba);
    
    return (ab >= ba) ? ab : ba;
}