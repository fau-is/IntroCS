#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int a = 10;
    int *p = &a;

    // Get / Print the address
    printf("%p\n", p);
    printf("%p\n", &a);

    // Print value of a
    printf("%i\n", *p);
    printf("%i\n", a);

    // Print address of P
    printf("%p\n", &p);
}
