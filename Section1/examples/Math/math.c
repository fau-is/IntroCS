#include <stdio.h>

int main(void)
{
    int a = 10;
    int b = 5;
    int c = 3;
    float d = 2.5;

    printf("%i + %i = %i\n", a, b, a + b);
    printf("%i - %i = %i\n", a, b, a - b);
    printf("%i * %i = %i\n", a, b, a * b);
    printf("%i / %i = %i\n", a, b, a / b);
    printf("%i %% %i = %i\n", a, b, a % b);
    printf("___________\n\n");

    printf("%i + %i = %i\n", a, c, a + c);
    printf("%i - %i = %i\n", a, c, a - c);
    printf("%i * %i = %i\n", a, c, a * c);
    printf("%i / %i = %i\n", a, c, a / c);
    printf("%i %% %i = %i\n", a, c, a % c);
    printf("___________\n\n");


    printf("%i + %.2f = %.2f\n", a, d, a + d);
    printf("%i - %.2f = %.2f\n", a, d, a - d);
    printf("%i * %.2f = %.2f\n", a, d, a * d);
    printf("%i / %.2f = %.2f\n", a, d, a / d);
    printf("___________\n\n");
}
