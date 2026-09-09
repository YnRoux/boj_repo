#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* my_string) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)calloc(52, sizeof(int));
    if (answer == NULL) {
        return NULL;
    }
    
    for (int i = 0; my_string[i] != '\0'; ++i) {
        char ch = my_string[i];
        if (ch >= 'A' && ch <= 'Z') {
            answer[ch - 'A']++;
        } else if (ch >= 'a' && ch <= 'z') {
            answer[ch - 'a' + 26]++;
        }
    }
    
    return answer;
}