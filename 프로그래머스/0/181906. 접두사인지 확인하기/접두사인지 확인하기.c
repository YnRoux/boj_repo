#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* my_string, const char* is_prefix) {
    size_t len_str = strlen(my_string);
    size_t len_pre = strlen(is_prefix);
    
    if (len_pre > len_str) {
        return 0;
    }
    
    if (strncmp(my_string, is_prefix, len_pre) == 0) {
        return 1;
    }
    
    return 0;
}