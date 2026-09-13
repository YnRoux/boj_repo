#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int price) {
    if (price >= 500000) {
        price = (int)(price * 0.80);
    } else if (price >= 300000) {
        price = (int)(price * 0.90);
    } else if (price >= 100000) {
        price = (int)(price * 0.95);
    }
    
    return price;
}