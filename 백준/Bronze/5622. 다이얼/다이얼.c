#include <stdio.h>
#include <string.h>

int main() {
    char word[20];
    scanf("%s", word);

    int len = strlen(word);
    int total_time = 0;

    for (int i = 0; i < len; i++) {
        char c = word[i];

        if (c >= 'A' && c <= 'C') {
            total_time += 3;
        } else if (c >= 'D' && c <= 'F') {
            total_time += 4;
        } else if (c >= 'G' && c <= 'I') {
            total_time += 5;
        } else if (c >= 'J' && c <= 'L') {
            total_time += 6;
        } else if (c >= 'M' && c <= 'O') {
            total_time += 7;
        } else if (c >= 'P' && c <= 'S') {
            total_time += 8;
        } else if (c >= 'T' && c <= 'V') {
            total_time += 9;
        } else if (c >= 'W' && c <= 'Z') {
            total_time += 10;
        }
    }

    printf("%d\n", total_time);

    return 0;
}