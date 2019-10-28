#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if (argc != 3)
 	{
        printf("Usage: ./babylon k a\n");
        return 1;
    }
    int k = atoi(argv[1]);
    int a = atoi(argv[2]);
    float eps = 0.01;

    if (k <= 0 || (a < 0 && (k % 2 == 0)))
    {
    	printf("Try again...\n");
    	return 1;
    }

    float xn;
    if (a < 0)
    {
    	xn = -2;
    } else 
    {
    	xn = 2;
    }

    float diff;
    do{
    	float xnhkm1 = 1;
    	float i = 0;
		while (i < k-1)
		{
			xnhkm1 = xnhkm1 * xn;
			i++;
		}

		float xnp1 = ((k - 1) * (xnhkm1 * xn) + a) / (k * xnhkm1);
		if (xn < xnp1)
		{
			diff = xnp1 - xn;
		} else
		{
			diff = xn - xnp1;
		}
		xn = xnp1;
    } while(diff > eps);
    
    printf("%.5f\n", xn);
    return 0;
}