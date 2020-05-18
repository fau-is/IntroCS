![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete getint.c
Write a program which uses the cs50 get_int() function to prompt a user for a input. You can 
also be creative and research by yourself whether there is a different way of reading in a user input in 
C as in the "real-world" CS50 functions won't always be available. We recommend looking at functions included in the <stdio.h> libraries.
You can find a plethora of information on specific libraries and its contained functions in the actual CS50 documentation 
or on W3Schools & other Development Websites available through the usage of your search-engine.

![creative](https://2.bp.blogspot.com/-izbeT9mH_Ko/XMWi-L9lsnI/AAAAAAAAAG4/klwUnirIoSwZyIfVfxpGwvdXfju5NW_1wCLcBGAs/s320/Drake%2B27042019210354.jpg)

Make sure that the input your program takes is between 0 - 100 inclusively. If this condition is met the program should 
print out the inputted number. If this is not the case there should be a re-prompt to input another number which satisifies the condition...or not.

~~~
Example: Input = 120; Output = 120 is not in between 0 -100
~~~

We have included some basic checks for you to see whether your program works in the intended way.
You can run this command in your Terminal to run the check
~~~
$check50 fau-is/IntroCS/Pset1/Getint --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset1/Getint
~~~

{% spoiler "Hints" %}

HINT: Make use of a While Loop or a do-while loop

{% endspoiler %}