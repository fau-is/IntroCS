#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>

int no_conv(int base, char* no);

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s base\n", argv[0]);
        return 1;
    }
    int base = atoi(argv[1]);

    printf("Number to convert: ");
    char *no = malloc(sizeof(char) * 21);

    scanf("%s", no);
    
    if(strlen(no) < 1)
    {
        return 2;
    }

    int result = no_conv(base, no);

    if(result == -1)
    {
        return 3;
    }
    
    printf("%d\n", result);

}

int no_conv(int base, char* no)
{
    int tmp_base = 1;
    int result = 0;
    for (int i = strlen(no) - 1; i > -1; i--)
    {
        
        int tmp = 0; 
        if (isdigit(no[i]))
        {
            tmp = (int) no[i] - 48;
        }
        else if(isalpha(no[i]))
        {
            if (isupper(no[i]))
            {
                tmp = 10 + ((int) no[i] - 65);
            }
            else
            {
                tmp = 10 + ((int) no[i] - 97);
            }
        }
        else
        {
            printf("Number System Not Convertible!\n");
            return -1;
        }
        result += tmp_base * tmp;
        tmp_base *= base; 
    }
    return result;
}
