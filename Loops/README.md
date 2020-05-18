![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete loops.c

    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            printf("i = %d, j = %d\n", i, j);

Transfer the code above into a program that uses only one for loop instead of a double for loop
Try not to use a while loop!

Think of the logic behind nested loops (loops in loops in loops...) and the effect it has on the
total times of iterating through specific code.

We have included some basic checks for you to see whether your program works in the intended way.
You can run this command in your Terminal to run the check
~~~
$check50 fau-is/IntroCS/Pset1/Loops --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset1/Loops
~~~


{% spoiler "Hints" %}

HINT: division and modulo can be helpful

{% endspoiler %}