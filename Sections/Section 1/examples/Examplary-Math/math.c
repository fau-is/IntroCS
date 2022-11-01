#include <stdio.h>

int main(void)
{
    int a = 10;
    int b = 5;
    int c = 3;
    float d = 2.5;

    printf("a + b = %i\n", a + b);
    printf("a - b = %i\n", a - b);
    printf("a * b = %i\n", a * b);
    printf("a / b = %i\n", a / b);
    printf("a %% b = %i\n", a % b);
    printf("___________\n\n");

    printf("a + c = %i\n", a + c);
    printf("a - c = %i\n", a - c);
    printf("a * c = %i\n", a * c);
    printf("a / c = %i\n", a / c);
    printf("a %% c = %i\n", a % c);
    printf("___________\n\n");


    printf("a + d = %.2f\n", a + d);
    printf("a - d = %.2f\n", a - d);
    printf("a * d = %.2f\n", a * d);
    printf("a / d = %.2f\n", a / d);
    printf("___________\n\n");
}
