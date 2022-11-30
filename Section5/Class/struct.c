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
        return 1;

    n->next = NULL;
    char *s = malloc(20);
    printf("%p\n", s);

    if(s == NULL)
        return 1;

    
    n->s = s;
    printf("%p\n", s);
    free(s);
    free(n);
}

