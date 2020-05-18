![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete lowupper.c

Write a Program that:
1. Reads a given array of chars.
2. Lowers capitalized letters (e.g. 'A' => 'a')
3. Capitalizes lower letters (e.g. 'a' => 'A')

The ASCII table might help you to figure out how you could convert the capitalization of the letters:

![ASCII Table](http://www.asciitable.com/index/asciifull.gif)



Functions from the *ctype.h* library might help you solve the task.
[Man-Page ctype.h](http://man7.org/linux/man-pages/man0/ctype.h.0p.html)

{% next "Output specification" %}

The output of your program should follow these specifications:
Given the array: 

```
    char array[] =  { 'A', 'b', 'C', 'd', 'E', 'f' };
```
The output for the given array should look as follows: 

```
    "[ a, B, c, D, e, F ]" 
```

We have included some basic checks for you to see whether your program works in the intended way.
You can run this command in your Terminal to run the check
~~~
$check50 fau-is/IntroCS/Pset2/Lowupper --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset2/Lowupper
~~~

