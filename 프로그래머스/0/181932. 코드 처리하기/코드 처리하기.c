#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* code) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int len = strlen(code);
    int alloc_len = len < 6 ? 6 : len + 1;
    char* answer = (char*)malloc(sizeof(char) * (alloc_len + 1));
    
    int mode = 0;
    int ans_idx = 0;
    
    for (int idx = 0; idx < len; ++idx) {
        if (code[idx] == '1') {
            mode = 1 - mode;
        } else {
            if (idx % 2 == mode) {
                answer[ans_idx++] = code[idx];
            }
        }
    }
    
    if (ans_idx == 0) {
        strcpy(answer, "EMPTY");
    } else {
        answer[ans_idx] = '\0';
    }
    
    return answer;
}