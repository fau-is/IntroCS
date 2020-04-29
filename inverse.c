/* Write a program that takes a command line input only allowing 1 Word. Use this command line input and make sure that the input
only consists of letters in the alphabet. Write your code to implement your alphabet check as a function outside of
your main Program. In your Program invert the input and print it out.
Example: Input = Hello; Output = olleH */

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