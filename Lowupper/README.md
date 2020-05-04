![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete lowupper.c

Write a Program that:
    1. Reads a given array of chars.
    2. Lowers capitalized letters (e.g. 'A' => 'a')
    3. Capitalizes lower letters (e.g. 'a' => 'A')

The ASCII table might help you to figure out how you convert the capitalization:

![ASCII Table](http://www.asciitable.com/index/asciifull.gif)

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

{% spoiler "Hints" %}

- Functions from the *ctype.h* library might help

{% endspoiler %}
