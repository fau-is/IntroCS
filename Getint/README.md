![fau-logo](https://introcs.is.rw.fau.de/img/logos/ReWi_logo.png)
# Complete getint.c
Write a program which uses CS50's _get_int()_ function to prompt a user for input. 
You can also research by yourself whether there are different ways of getting user input in 
C.
After this course, there will not be a CS50 library to support you. 
For the present purpose, the <stdio.h> library man page could be a good start.
You can find a plethora of information on specific libraries and its functions in the actual CS50 documentation, 
on W3Schools & other development websites.

![creative](https://2.bp.blogspot.com/-izbeT9mH_Ko/XMWi-L9lsnI/AAAAAAAAAG4/klwUnirIoSwZyIfVfxpGwvdXfju5NW_1wCLcBGAs/s320/Drake%2B27042019210354.jpg)

{% next "Program specs" %}

Make sure the input your program takes is between 0 - 100 inclusively. 
If the user input meets this condition the program should print out the following with the number provided by the user:

> $ ./getint
>
> Input: 10 
>
> Nice! The input was: 10

If the number is lower than 0 or greater than 100 you re-prompt the user to input another number.
Hopefully, this time the user satisfies your condition; otherwise you re-prompt again.

Example:
> $ ./getint
>
>Input: 120
>
>Nope! The input was: 120
>
>Input: 10
>
>Nice! The input was: 10

We have implemented basic checks for you. 
See whether your program works in the intended way!
You can run this command in the terminal to run the checks:
~~~
$ check50 fau-is/IntroCS/Pset1/Getint --local
~~~

**Note:** Don't forget the '\n' to start a new line when you provide output.

## Submit

You can submit your code to us via the following submit50 command:

~~~
$ submit50 fau-is/introcs/Pset1/Getint
~~~

{% spoiler "Hints" %}

HINT: Make use of a While Loop or a do-while loop

{% endspoiler %}
