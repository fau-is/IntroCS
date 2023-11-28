#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct node
{
    bool is_word;
    struct node *children[26];
}
node;

node *create(char *word);
bool add(node *trie, char* word, int len, int index);
bool find(node *trie, char *word, int len, int index);
void delete(node *trie);

int main(int argc, char *argv[])
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

    char buffer[100];

    node *trie = malloc(sizeof(node));
    if (trie == NULL)
    {
        return 3;
    }

    while(fscanf(f, "%s", buffer) == 1)
    {
        add(trie, buffer, strlen(buffer), 0);
        if (trie == NULL)
        {
            break;
        }
    }

    char *word = "Lorem";

    if(find(trie, word, strlen(word), 0))
        printf("Works\n");

    delete(trie);
}

bool add(node *trie, char* word, int len, int index)
{
    if (index < len)
    {
        if (trie->children[word[index] % 26] != NULL)
            return add(trie->children[word[index] % 26], word, len, index + 1);
        node *next = malloc(sizeof(node));
        if (next == NULL)
        {
            return false;
        }
        trie->children[word[index] % 26] = next;
        return add(next, word, len, index + 1);
    }
    else if (index == len)
    {
        trie->is_word = true;
        return true;
    }
    else
    {
        return false;
    }
}

bool find(node *trie, char *word, int len, int index)
{
    if (index > len || trie == NULL)
        return false;
    else if (index == len && trie->is_word == true)
        return true;
    else
        return find(trie->children[word[index] % 26], word, len, index + 1);

}

void delete(node *trie)
{
    if (trie == NULL)
        return;

    for (int i = 0; i < 26; i++)
    {
        delete(trie->children[i]);
    }
    free(trie);
}


