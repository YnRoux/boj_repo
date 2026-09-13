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

int solution(int n) {
    return n / get_gcd(n, 6);
}