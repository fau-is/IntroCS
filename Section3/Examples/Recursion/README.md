---
files: [recursion.c]
window: [terminal]
---
# Recursive Countdown

Recursion is a concept in programming where a function calls itself again.
Recursion can replace most Iterations.
Sometimes recursive functios can be easier to read than iterative loops.
On the right you see a program, which counts down from a certain number provided as command-line argument.


## Recursion Theory

A recursion must contain **at least one base case** and **at least one recursive case**.
A base case is a case, in which you know the result in advance, whereas a recursive case needs to be calculated.
A recursive case **must** contain a function-call to itself's function.


## Countdown
Let's take a look at countdown.

We find two base cases and one recursive case.

Base cases:
1. If *i* is negative, the program will just abort.
2. If *i* is *0*, the program prints "Go!".

In all other cases, the _recursive case_ is triggered.
Countdown will print _i_ and call _countdown(i-1)_, so we decrease _i_ by 1 for the next function call.


