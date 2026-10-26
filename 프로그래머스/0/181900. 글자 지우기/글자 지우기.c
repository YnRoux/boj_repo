#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// indices_len은 배열 indices의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, int indices[], size_t indices_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int str_len = strlen(my_string);
    int result_len = str_len - indices_len;
    
    bool is_deleted[100] = {false, };
    for (size_t i = 0; i < indices_len; ++i) {
        is_deleted[indices[i]] = true;
    }
    
    char* answer = (char*)malloc(sizeof(char) * (result_len + 1));
    
    int idx = 0;
    for (int i = 0; i < str_len; ++i) {
        if (!is_deleted[i]) {
            answer[idx++] = my_string[i];
        }
    }
    
    answer[idx] = '\0';
    
    return answer;
}