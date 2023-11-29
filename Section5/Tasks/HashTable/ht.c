#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *hashtable[15];

int hash_function(char *word);
void add(char *word);
void find(char *word);
void size();
void delete();


int main(void)
{
    char buffer[30];
    for (int i = 0; i < 5; i++)
    {
        scanf("%s", buffer);
        add(buffer);
    }
    find("Hello");
    size();

    delete();
}


int hash_function(char *word)
{
    int bucket = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        bucket += word[i];
    }
    return bucket % 15;
}

void add(char *word)
{
    int bucket = hash_function(word);

    while(hashtable[bucket] != NULL)
    {
        bucket = (bucket + 1) % 15;
    }

    hashtable[bucket] = malloc(strlen(word));
    if (hashtable[bucket] == NULL)
        return;
    strcpy(hashtable[bucket], word);

}

void find(char *word)
{
    int bucket = hash_function(word);
    int counter = 0;
    while(hashtable[bucket] == NULL || strcmp(hashtable[bucket], word) != 0)
    {
        bucket = (bucket + 1) % 15;
        counter++;
        if (counter > 15)
        {
            printf("Not found\n");
            return;
        }
    }
    printf("Found\n");
}

void size()
{
    for (int i = 0; i < 15; i++)
    {
        if (hashtable[i] != NULL)
        {
            printf("%i: 1\n", i);
        }
        else
        {
            printf("%i: 0\n", i);
        }
    }
}

void delete()
{
    for (int i = 0; i < 15; i++)
    {
        if (hashtable[i] != NULL)
            free(hashtable[i]);
    }
}
