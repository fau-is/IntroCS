#include <stdio.h>
#include <stdlib.h>

int A[10] = {3, 200, 30, 20, 49, 34, 60, 1, 9, 10};

typedef struct node
{
    int payload;
    struct node *next;
}
node;

void pretty_printer(node *root)
{
    node *trav= malloc(sizeof(node));
    if(trav == NULL)
    {
        exit(0);
    }
    trav = root;
    for (int i = 1; i < sizeof(A) / sizeof(int) + 1; i++)
    {
        int n = trav->payload;
        printf("Payload %d = %d\n", i, n);
        trav = trav->next;
    }
}

void free_ll(node *head)
{
    //ToDo
}

int main(void) {
    node *root = malloc(sizeof(node));
    if (root == NULL) {
        return 1;
    }
    root->payload = A[0];
    root->next = NULL;

    //ToDo

    pretty_printer(root);
    free_ll(root);

    return 0;
}