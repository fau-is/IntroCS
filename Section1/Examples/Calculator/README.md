---
files: [calculaor.c]
window: [terminal]
---
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

{% next File outline %}

## File outline
### Header
In a program's header, we will find include statements.
Include statements are used to import code from librarys.

- stdio.h
  - Required to print results to the command line.
  - Preinstalled in most operating systems.
- cs50.h
  - CS50's training wheels is imported to make your life a little easier in the beginning.

### Prototypes
You need to use function prototypes, if you want to have your main function on top of the program; at least relatively.

In calculator.c, we using functions to calculate our results. And, we are using a dedicated print function. You can find their implementations below the main function.

### Main Function
The heart of your program is the main-function. Every program needs a main function to compile. For now, your main functions could look as follows:
```C
 int main(void)
```
The first thing your program actively does is the first line in your main function.
From here, you could call other functions, fulfill your tasks, or just print "Hello, world".

### Functions
Functions have a return value, and often they require parameters. Both, the return type and the parameters require specifications of a data type.

Assume, there is the following function sum:
```C
> int sum(int a, int b)
{
  return a + b;
}
```

This function must return an integer to its caller, e.g., the main-function. Additionally, this function always expects two Integer values as parameters.

{% next "Try running calculator" %}

## Try the program
Despite not being the most usable calculator, this minimal example shows: You can already write and understand a program.

By now, you should be able to run a program on your own.
Still, if you need help click the button below to see instruction on how to run the program.

{% spoiler "How to run" %}
```bash
make calculator
./calculator
```
{% endspoiler %}
