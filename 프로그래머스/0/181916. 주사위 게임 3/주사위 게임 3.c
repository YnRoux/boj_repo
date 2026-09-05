#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int solution(int a, int b, int c, int d) {
    int dice[4] = {a, b, c, d};
    qsort(dice, 4, sizeof(int), compare);
    
    if (dice[0] == dice[3]) {
        return 1111 * dice[0];
    }
    
    if (dice[0] == dice[2]) {
        int p = dice[0];
        int q = dice[3];
        return (10 * p + q) * (10 * p + q);
    }
    
    if (dice[1] == dice[3]) {
        int p = dice[1];
        int q = dice[0];
        return (10 * p + q) * (10 * p + q);
    }
    
    if (dice[0] == dice[1] && dice[2] == dice[3]) {
        int p = dice[0];
        int q = dice[2];
        return (p + q) * abs(p - q);
    }
    
    if (dice[0] == dice[1]) {
        return dice[2] * dice[3];
    }
    
    if (dice[1] == dice[2]) {
        return dice[0] * dice[3];
    }
    
    if (dice[2] == dice[3]) {
        return dice[0] * dice[1];
    }
    
    return dice[0];
}