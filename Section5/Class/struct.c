#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    char *s;
    struct node* next;
}
node;

int main(void)
{
    node *n = NULL;


    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->next = NULL;
    char *s = malloc(20);
    s = "hello";
    n->s = s;
    printf("%s\n", n->s);
    free(s);
    free(n);
}

