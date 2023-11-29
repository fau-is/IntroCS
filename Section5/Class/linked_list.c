#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

typedef struct node
{
    int value;
    struct node *next;
} node;

node *create(int value);
node *add(node *list, int value);
bool find(node *list, int to_find);
bool delete_node(node *list, int to_find);
void delete(node *list);
int size(node *list);
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
    // print_list(list);
    printf("%i numbers were read.\n", size(list));
    // delete(list);
}

node *create(int value)
{
    node *new = malloc(sizeof(node));
    if (new == NULL)
    {
        return new;
    }

    new->value = value;
    new->next = NULL;
    return new;

}

node *add(node *list, int value)
{
    node *new_head = create(value);
    if (new_head == NULL)
    {
        delete(list);
        return NULL;
    }
    new_head->next = list;
    return new_head;
}

void delete(node *list)
{
    if (list == NULL)
    {
        return;
    }
    delete(list->next);
    free(list);
}

bool find(node *list, int to_find)
{
    node *cursor = list;
    while(cursor != NULL)
    {
        if (cursor->value == to_find)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

int size(node *list)
{
    int size = 0;
    for (node *cursor = list; cursor != NULL; cursor = cursor->next)
    {
        size++;
    }
    return size;
}

void print_list(node *list)
{
    for (node *cursor = list; cursor != NULL; cursor = cursor->next)
    {
        printf("%i -> ", cursor->value);
    }
    printf("\n");
}



