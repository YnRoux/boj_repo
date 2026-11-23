#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    
    int sum = 0;
    
    char str[101];
    scanf("%s", str);
    
    for (int i = 0; i < n; i++)
    {
        sum += str[i] - '0';
    }
    
    printf("%d", sum);
    return 0;
}