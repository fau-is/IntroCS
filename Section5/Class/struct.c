#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    char *s;
    struct node* next;
}
node;

int main(int argc, char **argv)
{
    node *n = NULL;

    while(1)
    {
        n = malloc(sizeof(node));
        if (n == NULL)
        {
            break;
        }
        n->next = NULL;
        char *s = malloc(20);
        s = "hello";
        n->s = s;
        printf("%s %s\n", s, n->s);
        free(n);
    }

}