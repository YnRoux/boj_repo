#include <iostream>
#include <string>
#include <cctype> // 문자 관련 함수(대소문자 판별 등)를 쓰기 위한 도구 상자

using namespace std;

int main() {
    string str;
    cin >> str; // 입력 받기

    // 문자열의 길이만큼 반복하기
    for (int i = 0; i < str.length(); i++) {
        
        // 현재 글자가 대문자인지 확인
        if (isupper(str[i])) {
            // 대문자면 대문자 -> 소문자
            cout << (char)tolower(str[i]);
        }
        else{
            // 아니면(소문자) 소문자 -> 대문자
            cout << (char)toupper(str[i]);
        }
    }
    return 0;
}