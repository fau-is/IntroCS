#include <stdio.h>

typedef struct node
{
    char *s;
    struct node* next;
}
node;

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        printf("Usage: %s [Names]", argv[0]);
        return 1;
    }

    for (int i = 1; i < argc; i++)
    {
        
    }

}