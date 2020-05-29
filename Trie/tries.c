#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char A[9][10] = {"Paris", "Erlangen", "Nuernberg", "Bamberg", "Montenegro", "Muenchen", "Bayreuth", "Ingolstadt", "Ansbach"};

#define N 27
#define size 9
#define LENGTH 45

typedef struct node
{
    bool is_city;
    struct node *children[N];
}
node;

node *root;

int count = 0;

unsigned int counting(node *temp)
{
    //ToDo
    return count;
}

bool check(const char *word)
{
    //ToDo
}

void unload(node *temp)
{
    //ToDo
}

int main(void)
{
    char *cities = "Test.txt";
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        return false;
    }
    root->is_city = false;
    for (int i = 0; i < N; i++)
    {
        root->children[i] = NULL;
    }

    FILE *file = fopen(cities, "r");
    if (file == NULL)
    {
        unload(root);
        return false;
    }

    char word[LENGTH + 1];

    //ToDo

    node *temp = root;
    printf("Cities in Trie: %i\n", counting(temp));
    for (int i = 0; i < size; i++)
    {
        if (check(A[i]) == false)
        {
            printf("%s is not in Trie\n", A[i]);
        }
    }
    temp = root;
    unload(temp);
    fclose(file);
    return 0;
}