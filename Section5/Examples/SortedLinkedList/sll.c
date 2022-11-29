#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct node
{
    int payload;
    struct node *next;
}
node;

node *create(int value);
node *add(node *list, int value);
bool find(node *list, int value);
bool delete(node *list);
void print_list(node *list);

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s filepath\n", argv[0]);
        return 1;
    }

    node *list = create(arr[0]);

    if (list == NULL)
    {
        return 1;
    }

    FILE *f = fopen(argv[1], "r");

    if (f == NULL)
    {
        printf("Path %s does not exist\n", argv[1]);
        return 2;
    }

    int i;

    while(fscanf(f, "%i", &i) == 1)
        list = add(list, i);

    fclose(f);

    print_list(list);
    delete(list);
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
    if (list == NULL)
        return create(value);
        
    node *new = create(value);
    if (new != NULL)
    {
        node *cursor = list;
        while(cursor->next != NULL)
        {
            if (cursor->payload > value)
            {
                new->next = list;
                return new;
            }
            if ((cursor->next->payload > value && cursor->payload < value) || cursor->payload == value)
            {
                new->next = cursor->next;
                cursor->next = new;
                return list;
            }
            cursor = cursor->next;
        }
        cursor->next = new;
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

bool delete(node *list)
{
    if (list == NULL)
        return true;
    delete(list->next);
    free(list);
    if(list == NULL)
        return true;
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



