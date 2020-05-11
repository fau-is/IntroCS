![fau-logo](https://www.fau.de/files/2016/02/fb-ww-logo-preview.jpg)
# Complete wizardry.c

## Wizardry
In this exercise you will implement a program which reads in an input file and copies its
contents to an output file. Furthermore, you will be required to manipulate the content
being written into your output file. To be more specific you will be receiving your very
own personal letter of invitation to Hogwarts!

**In this exercise, don't worry about Special signs e.g. "!, [, ., ;" etc. We'll just look at
strings in their entirety.**

{% next %}
## Program Specifications
You have again received some distribution code on which you are required to build. Furthermore,
in this exercise instead of one file we have provided you with 3 files in total. 

1. **wizardry.c** - this is your program file where you will do all of your coding.
2. **hogwarts.txt** - this is your input .txt file which you are required to read in
3. **myletter.txt** - this is you output .txt. file which you will write into

For this exercise you must be familiar with all the functions introduced by CS50s included
in FILE I/O.

Your program should take in 3 command line arguments which it can use throughout. Your
first command line argument should be the input file. The second one should be the output file
and lastly you should also give your Surname.
~~~
./wizardry hogwarts.txt myletter.txt Surname
~~~
If your program detects more or less than 3 command line arguments it should behave
as follows.
~~~
Output: ./wizardry infile outfile name
~~~

The first step which you will have to take is to actually open both relevant .txt files.
Do not forget to check whether they actually exist! Furthermore, if you open a file at the
end of your program you should close said file in order to avoid a memory leak!

After opening both files we want you to write the contents of hogwarts.txt into myletter.txt.
However, there is one further hurdle you will have to jump for success.
The first line in hogwarts.txt is:
~~~
Dear Mr/Ms. Surname,
~~~
We don't want your myletter.txt to look the same! We want your very own personalized
letter of acceptance! Therefore the first line in your myletter.txt file should look like
the above however, instead of 'Surname' we want to have your name in its place. To be even 
more specific the name that will be read in as the 3rd command line argument of your program.



{% next "Library Talk" %}

## Libraries