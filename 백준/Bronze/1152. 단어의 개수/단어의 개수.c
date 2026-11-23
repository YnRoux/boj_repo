#include <stdio.h>
#include <string.h>

char str[1000005];

int main() {
    fgets(str, sizeof(str), stdin);
    
    int len = strlen(str);
    
    if (len > 0 && str[len - 1] != '\0')
    {
        str[len - 1] = '\0';
        len--;
    }
    
    int count = 0;
    
    for (int i = 0; i < len; i++)
    {
        if (str[i] != ' ')
        {
            if (i == 0 || str[i - 1] == ' ')
            {
                count++;
            }
        }
    }
    
    printf("%d\n", count);
    return 0;
}