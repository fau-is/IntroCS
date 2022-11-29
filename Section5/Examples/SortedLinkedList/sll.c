#include <stdio.h>
#include <stdlib.h>


typedef struct node
{
    int payload;
    struct node *next;
}
node;

node *create(int value);
node *add(node *list, int value);
bool find(node *list, int value);
bool delete(node *list, int value);
void print_list(node *list);

int main(int argc, char **argv)
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7};

    node *list = create(arr[0]);

    if (list == NULL)
    {
        return 1;
    }

    for (int i = 1, len = 7; i < len; i++)
    {
        list = add(list, arr[i]);
    }


}


node *create(int value)
{
    node *n = malloc(sizeof(node));

    if (n == NULL)
    {
        return NULL;
    }

    n->payload = value;
    n->next = NULL;

    return n;
}


node* add(node *list, int value)
{
    node *new = create(value);
    if (new != NULL)
    {
        new->next = list;
        return new;
    }
    return list;
}


bool find(node *list, int value)
{
    for (node* cursor = list; cursor != NULL; cursor = cursor->next)
    {
        if (cursor->payload == value)
        {
            return true;
        }
    }
    return false;
}

void print_list(node *list)
{
    printf("->");

    for (node *cursor = list; cursor != NULL; cursor = cursor->next)
    {
        printf("%i->", cursor->payload);
    }
    printf("\n");

}



