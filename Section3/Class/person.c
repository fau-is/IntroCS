#include <stdio.h>
#include <cs50.h>

typedef struct
{
    string first_name;
    string last_name;
}
person;

int main(void)
{
    person p1;
    p1.first_name = "Sebastian";
    p1.last_name = "Dunzer";

    person p2;
    p2.first_name = "Daniel";
    p2.last_name = "Schraudner";

    person arr[2] = {p1, p2};

    for (int i = 0; i < 2; i++)
        printf("%s %s\n", arr[i].first_name, arr[i].last_name);

}
