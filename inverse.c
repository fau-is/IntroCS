#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int alphabet(char *word, int size);

int main(int argc, char **argv)
{
  if (argc != 2)
  {
    printf("Enter Word\n");
    return 1;
  }
  char *word = argv[1];
  int size = strlen(word);

  if (alphabet(word, size) == 1)
  {
    return 1;
  }

  char inverse[size];
  for (int j = 0; j < size; j++)
  {
    inverse[j] = word[size - 1 - j];
  }
  printf("inverse: %s\n", inverse);
  return 0;
}

int alphabet(char *word, int size)
{
  for (int i = 0; i < size; i++)
  {
    if (isalpha(word[i]) == 0)
    {
      printf("Input word\n");
      return 1;
    }
  }
  return 0;
}