#include <stdio.h>

void start_end_char()
{
    char str[1001];
    scanf("%s", str);
    
    int i = 0;
    while (str[i] != '\0')
    {
        i++;
    }
    
    printf("%c%c\n", str[0],str[i-1]);
    return;
}

int main()
{
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++)
    {
        start_end_char();
    }
    
    return 0;
}