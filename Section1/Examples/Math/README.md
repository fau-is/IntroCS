---
files: [maht.c]
window: [terminal]
---
# Some Math in C

The programming language C provides all basic Math operators.
Let's have a look at the program to the right.

First we're defining some variables. Most of them are of the type int (Integer).
For completeness, there is one variable pre-defined to show how float calculations work out.

The basic operators in C are:
- '+' Plus
- '-' Minus
- '*' Multiply
- '/' Division
    - Important: Floor division
    - Dividing int(s) 1 by 2 will result in 0, not in 0.5
- '%' Modulo
    - Returns the remainder of a division
    - e.g. 10 / 3 = 3 with a *remainder of 1*

Data type specifics:
- If you require a non natural number, one side of your calculation AND the result need to be either float, or double
- If you are handling very large numbers, int may run out of place. In such cases, use the long datatype.


