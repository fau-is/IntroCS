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
    if (argc < 2)
    {
        printf("Usage: %s [Names]", argv[0]);
        return 1;
    }
    node *n = NULL;

    for (int i = 1; i < argc; i++)
    {
        n = malloc(sizeof *n);
        n->next = NULL;
        n->s = argv[i];
        argv[i] = "Oh No!";
        printf("%s\n", n->s);
        free(n);
    }

}