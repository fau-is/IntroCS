#include <stdio.h>

typedef struct
{
    float width;
    float height;
}
rectangle;

float calc_area(float width, float height)
{
    return width * height;
}

float calc_peri(float width, float height)
{
    return width * 2 + height * 2;
}

int main(void)
{
    rectangle rect;
    rect.width = 10;
    rect.height = 10;

    float area = calc_area(rect.width, rect.height);
    float perimeter = calc_peri(rect.width, rect.height);

    printf("%f.2", square);
    printf("%f.2", perimeter);
}