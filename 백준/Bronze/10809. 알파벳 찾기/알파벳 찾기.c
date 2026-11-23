#include <string.h>

int main() {
    char s[101];
    int pos[26];

    for (int i = 0; i < 26; i++) {
        pos[i] = -1;
    }

    scanf("%s", s);
    int len = strlen(s);

    for (int i = 0; i < len; i++) {
        int idx = s[i] - 'a';
        if (pos[idx] == -1) {
            pos[idx] = i;
        }
    }

    for (int i = 0; i < 26; i++) {
        printf("%d ", pos[i]);
    }

    return 0;
}