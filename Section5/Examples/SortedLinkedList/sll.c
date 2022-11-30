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
int size(node *list);
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

    FILE *f = fopen(argv[1], "r");

    if (f == NULL)
    {
        printf("Path %s does not exist\n", argv[1]);
        return 2;
    }

    int i;
    node *list;

    while(fscanf(f, "%i", &i) == 1)
    {
        list = add(list, i);
        if (list == NULL)
        {
            break;
        }
    }

    fclose(f);

    print_list(list);
    printf("%i Numbers were read\n", size(list));
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
    if (new == NULL)
        return list;

    node *cursor = list;
    while(cursor->next != NULL)
    {
        if (new->payload < cursor->payload)
        {
            new->next = list;
            return new;
        }
        else if (new->payload >= cursor->payload && new->payload < cursor->next->payload)
        {
            new->next = cursor->next;
            cursor->next = new;
            return list;
        }
        cursor = cursor->next;
    }
    cursor->next = new;
    return list;
}

int size(node *list)
{
    if (list == NULL)
        return 0;
    return size(list->next) + 1;
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



