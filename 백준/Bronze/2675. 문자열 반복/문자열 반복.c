#include <stdio.h>
#include <string.h>

void rep_char()
{   
    int n;
    scanf("%d", &n);
    char str[21];
    scanf("%s", str);
    int len = strlen(str);
    
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%c", str[i]);
        }
    }
    printf("\n");
    
    return;
}

int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++)
    {
        rep_char();
    }
    
    return 0;
}