# Addition

Write a program addition.c that sums up two numbers provided as command-line arguments.

Specs:
- The program should accept two integers as command-line arguments.
- The program should output both original numbers, and their sum.
    - If the program is run as ‘./addition 2 8’ for example, the output should be 2 + 8 = 10.
- If the incorrect number of command-line arguments is provided, the program should display an error and return with exit code 1.

Hints:
- Provide the appropriate exit codes
- Command-line arguments
- ‘int atoi(string s)’ from stdlib.h converts a string to an integer.
