# String builder
If strings are arrays of characters, we should be able to rebuild a string using our own char array.

## File outline
Includes:
- Stdio - For printing to the commandline
- CS50-library to get a string from the commandline
- String.h for some functions related to strings
    - strlen(s) to get the length of a string
    - strcmp(s1,s2) to compare two strings with each other

Main funtion (Pseudo)
1. Get_string s from user to rebuild
2. Create char array t with length of s + 1, for the \0 character.
3. For length of s from 0
    1. copy char from s to t each at index i
4. If strings are equal
    1. Quit program
5. Else
    1. Add \0 character to t at length of s as index
    2. Check if strings are equal
        1. If strings are equal: Exit Code 0
        2. Else: Exit Code 1

## Some Explanation
Consider the following string s:

```C
    string s = "Hi";
```

Under the hood, the characters of s are stored in a char array:

```C
    char s[] = {'H', 'i'}
```

However in C there is not and indication of how many characters are contained within an array.
The only value stored within c is the location of the first character ('H') in memory.
Therefore, the language C indicates the end of a string with a special character, the _NUL character (\0)_

The representation of string s actually looks like the following array:

```C
    char s[] = {'H', 'i', '\0'}
```

For simplicity, let us assume all bytes have a unique address as a decimal number.
Consider the character 'H' of s is stored at address 123.
Then, the program does not even know, that the character 'i' of s is following at address 124 and address 125 stores the NUL character.

To understand how a computer handles this issue, let us consider the following function-call, which we used plenty of times already:
```C
    printf("%s", s);
```

_%s_ indicates to printf that it is looking for a string (i.e. a series of characters).
Printf will look at the known address 123 of 'H' and print the character. Then, it will look at address 124 and print character 'i', as it is stored there. Lastly, the program will look at the next address 125 and find a NUL character.
This NUL character indicates, that the string ends here and the forward lookup ends here.

For better imagination, let's look at how this sequency could look like.
```C
    string s = "Hi";
    char c = s[0]; // Go to address of s (same as s[0])
    while (c != '\0')
    {
        printf('%c', c); // Print only one character
        c = s[1];
    }
```
This loop would print Hi.

## Warning
A lot of unused bytes is actually full of NUL characters as it consists of 8 0-bits (00000000). Often, even if you forget to set a NUL character, your string handling will work as you expected, because your string is followed by random memory which is empty (i.e. consists of NUL characters).

Consider the following simplified situations.

### Situation: Code works (randomly) without \0
You initialise a char array and an Integer:
```C
    char c[] = {'I','N','T','R','O'}; // 5 Bytes
    int i = 0; // 4 Bytes
```
Assume that:
- _c_ is stored at addresses 0-4;
- _i_ is stored at 5-8

Now if you map the addresses...
- 0: I
- 1: N
- 2: T
- 3: R
- 4: O
- 5: 00000000 (first byte of integer)
- 6: 00000000
- 7: 00000000
- 8: 00000000

... and look at 5, we see that it contains the \0 character (8 x 0-bit)
So, this string will be handled perfectly!
*BUT: Programs which randomly work are BAD!*

#### Situations in which it does not work










