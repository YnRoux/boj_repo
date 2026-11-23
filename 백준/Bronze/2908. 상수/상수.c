#include <stdio.h>
#include <string.h>

int main() {
    char a[4], b[4];
    scanf("%s %s", a, b);
    
    char temp = a[0];
    a[0] = a[2];
    a[2] = temp;
    
    temp = b[0];
    b[0] = b[2];
    b[2] = temp;
    
    if (strcmp(a, b) > 0)
    {
        printf("%s\n", a);
    }
    else
    {
        printf("%s\n", b);
    }
    
    return 0;
}