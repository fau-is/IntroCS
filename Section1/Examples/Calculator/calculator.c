#include <stdio.h>
#include <cs50.h>

// Functions
void print_result(char c, int a, int b, int d);
int sum(int a, int b);
int modulo(int a, int b);
int multiply(int a, int b);
int division(int a, int b);
void mean();
int quit();

int main(void)
{
    char action;

    while(true)
    {
        action = get_char("What do you want to do? \n\ta(ddition) \n\ts(ubstraction) \n\tp(roduct) \n\td(ivision) \n\tr(emainder)\n\tm(ean)\n\tq(uit)\nAction: ");

        if(action == 'q')
        {
            return 0;
        }

        if (action == 'm')
        {
            mean();

            if (quit() == 1)
            {
                return 0;
            }

            continue;
        }

        int a = get_int("a = ");
        int b = get_int("b = ");

        if (action == 'a')
        {
            print_result('+', a, b, a + b);
        }
        else if(action == 's')
        {
            print_result('-', a, b, a - b);
        }
        else if(action == 'p')
        {
            print_result('*', a, b, a * b);
        }
        else if(action == 'd')
        {
            print_result('/', a, b, division(a, b));
        }
        else if(action == 'r')
        {
            print_result('%', a, b, modulo(a, b));
        }


        if (quit() == 1)
        {
            return 0;
        }

    }
}

void print_result(char c, int a, int b, int d)
{
    printf("Result:\n");
    printf("%i %c %i = %i\n", a, c, b, d);
}

int sum(int a, int b)
{
    return a + b;
}

int modulo(int a, int b)
{
    int rem = a;

    while(rem >= b)
    {
        rem = rem - b;
    }

    return rem;
}

int division(int a, int b)
{
    int rem = a;
    int counter = 0;
    while(rem >= b)
    {
        rem = rem - b;
        counter++;
    }
    return counter;
}

int multiply(int a, int b)
{
    int result = 0;
    for (int i = 0; i < a; i++)
    {
        result = result + b;
    }
    return result;
}

void mean()
{
    int sum = 0;
    int numbers = get_int("How many values? ");

    for (int i = 0; i < 10; i++)
    {
        sum += get_int("Value: ");
    }


    printf("Average: %.2f\n", sum / 10.0);
}

int quit()
{
    do
    {
        char action = get_char("Continue? y / n? ");

        if(action == 'y' || action == 'Y')
        {
            return 0;
        }
        if(action == 'n' || action == 'N')
        {
            return 1;
        }
    }
    while(true);
}

