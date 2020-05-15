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

void delete_ll(node *head)
{
    node *curr = malloc(sizeof(node));
    if (curr == NULL)
    {
        exit(1);
    }

    while ((curr = head) != NULL)
    {
        head = head->next;
        free (curr);
    }
}

int main(void) {
    node *root = malloc(sizeof(node));
    if (root == NULL) {
        return 1;
    }
    root->payload = A[0];
    root->next = NULL;

    node *temp = malloc(sizeof(node));
    if (temp == NULL)
    {
        return 1;
    }
    temp = root;
    for (int i = 1; i < sizeof(A) / sizeof(int); i++)
    {
        node *current = malloc(sizeof(node));
        if (current == NULL)
        {
            return 1;
        }

        current->payload = A[i];
        current->next = NULL;

        if (temp->next == NULL)
        {
            temp->next = current;
        }
        else
        {
            temp = temp->next;
            while (temp->next != NULL)
            {
                temp = temp->next;
            }
            temp->next = current;
        }
    }
    pretty_printer(root);
    delete_ll(root);

    return 0;
}








