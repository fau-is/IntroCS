#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char A[7][10] = {"Erlangen", "Nuernberg", "Bamberg", "Muenchen", "Bayreuth", "Ingolstadt", "Ansbach"};

#define N 27
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
    if(temp->is_city == true)
    {
        count++;
    }
    for(int i = 0; i < N; i++)
    {
        if(temp->children[i] != NULL)
        {
            counting(temp->children[i]);
        }
    }
    return count;
}

bool check(const char *word)
{
    node *pointer = root;
    for (int j = 0; j <= strlen(word); j++)
    {
        int index = tolower(word[j]) - 'a';
        if (word[j] != '\0')
        {
            if (pointer -> children[index] == NULL)
            {
                return false;
            }
            else
            {
                pointer = pointer -> children[index];
            }

            if (pointer -> is_city == true)
            {
                return true;
            }
        }
    }
    return false;
}

void unload(node *temp)
{
    for(int i = 0; i < N; i++)
    {
        if(temp->children[i] != NULL)
        {
            freeTrie(temp->children[i]);
        }
    }
    free(temp);
}

int main(void)
{
    int size = 7;
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
        unload();
        return false;
    }

    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        int length = strlen(word);
        node *current = root;
        printf("%s\n", word);
        for(int i = 0; i < length; i++)
        {
            int index = tolower(word[i]) - 'a';
            printf("%c", word[i]);

            if (current -> children[index] == NULL)
            {
                node *pNode = malloc(sizeof(node));
                if (pNode == NULL)
                {
                    return false;
                }
                current->children[index] = pNode;
                current = pNode;
            }
            else
            {
                current = current->children[index];
            }
        }
        current -> is_city = true;
        printf("\n");
    }
    node *temp = root;
    printf("Cities in Trie: %i\n", counting(temp));
    for (int i = 0; i < size; i++)
    {
        if (check(A[i]) == false)
        {
            printf("City is not in Trie");
        }
    }
    temp = root;
    unload(temp);
    fclose(file);
    return 0;
}