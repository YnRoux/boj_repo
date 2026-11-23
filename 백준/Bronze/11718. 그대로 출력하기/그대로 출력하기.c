#include <stdio.h>

int main() {
    char line[105];
    while (fgets(line, sizeof(line), stdin) != NULL) {
        printf("%s", line);
    }
    return 0;
}