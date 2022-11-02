# Let's have a look at a very basic program: A calculator

## Intro
If we combine loops, functions and getting input from users, we can create a first program.
For now, let's not argue about usefulness ;).

## Functionality
In every loop, the program will ask which calculator operation should be executed. Depending on a user's input a function is called:
- sum
- modulo
- multiply
- division

After performing the calculation the result is printed.

{%next File outline %}

## File outline
### Header
In a program's header, we will find include statements.
Include statements are used to import code from librarys.


- <stdio.h>
  - Required to print results to the command line.
  - Preinstalled in most operating systems.
- <cs50.h>
  - CS50's training wheels is imported to make your life a little easier in the beginning.


