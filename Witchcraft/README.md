---
files: [wizardy.c]
window: [terminal]
---
![fau-logo](https://introcs.is.rw.fau.de/img/logos/ReWi_logo.png)
# Complete wizardry.c

## Wizardry
In this exercise, you will implement a program that reads in an input file and copies its
contents to an output file. Furthermore, you will be required to manipulate the content
being written into your output file. To be more specific you will be receiving your very
own personal letter of invitation to Hopwarts!

For this exercise, you must be familiar with all the functions introduced by CS50 included
in FILE I/O. If you are unsure where to start have a look at the functions included in the
stdio.h library 

[stdio.h](https://www.tutorialspoint.com/c_standard_library/stdio_h.htm)

**In this exercise, don't worry about Special signs e.g. "!;  [;  .;  $;  =" etc. We'll just look at
strings in their entirety.**

{% next %}
## Program Specifications
You have again received some distribution code on which you are required to build. Furthermore,
in this exercise instead of one file, we have provided you with 3 files in total. 

1. **wizardry.c** - this is your program file where you will do your programming.
2. **hopwarts.txt** - this is your input .txt file which you are required to read in
3. **myletter.txt** - this is you output .txt. file which you will write into


Your program should take in 3 command-line arguments which it can use throughout. Your
first command-line argument should be the input file. The second one should be the output file
and lastly, you should also give your Surname.
~~~
./wizardry hopwarts.txt myletter.txt Surname
~~~
If your program detects more or less than 3 command-line arguments it should behave
as follows.
~~~
Output: ./wizardry infile outfile name
~~~

The first step which you will have to take is to actually open both relevant .txt files.
Do not forget to check whether they actually exist! Furthermore, if you open a file at the
end of your program you should close the said file in order to avoid a memory leak!

After opening both files we want you to write the contents of hogwarts.txt into myletter.txt.
However, there is one further hurdle you will have to jump for success.
The first line in hopwarts.txt is:
~~~
Dear Mr/Ms. Surname,
~~~
We don't want your myletter.txt to look the same! We want your very own personalized
letter of acceptance! Therefore, the first line in your myletter.txt file should look like
the above, however, instead of 'Surname' we want to have your name in its place. To be even
more specific the name that will be read in as the 3rd command line argument of your program.

There are some prerequisites to do that. To actually replace or change the content you are 
reading in and writing out. You must compare whether the string or character you are
currently reading in is actually the same as the string you want to replace it with. 
For this purpose, we want to recommend the **strstr()** function. This function searches for
a substring within an existing string.
~~~
string = "This is Intro CS!";
substring = "CS!";
~~~
We strongly recommend that you look at the function's documentation online. 
As soon as you understand its usage, it will make your life a lot easier!

To sum up: As soon as you have completed the task your myletter.txt file should look
like this - if your name is Garry Hotter!

~~~
Dear Mr/Ms. Hotter,

We are pleased to inform you that you have been accepted at Hopwarts School of Witchcraft and Wizardry.
Please find enclosed a list of all necessary books and equipment.
The term begins on 1st of September. We await your owl by no later than 31st of July.
Yours sincerely,

Inmerva McAgonall
Deputy Headmistress
~~~

**Have fun coding!**

![yer_a_wizard](http://27.media.tumblr.com/tumblr_lpjqjvBJ8y1qk68p2o1_500.gif)


{% next "Library Talk" %}

## Libraries

  
You find functions that will help you with this task in the *stdio.h* library.
Other than that all the libraries you need are included in the header already.

If you don't know which library contains what function, you find a plethora of documentation for C 
libraries in the actual CS50 documentation, GeekForGeeks, and W3Schools.

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/Pset3/Witchcraft --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset3/Witchcraft
~~~
