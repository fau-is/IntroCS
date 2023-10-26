---
files: [101.c]
window: [terminal]
---
# Double For-Loop (101.c)

Write that prints out the small multiplication table.

> $ ./101\
> 1&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;10\
> 2&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;10&nbsp;&nbsp;12&nbsp;&nbsp;14&nbsp;16&nbsp;18&nbsp;&nbsp;20\
> ...\
> 10   20  30  40  50  60  70  80  90  100

{% spoiler "Pseudo Solution" %}
- For character alignment you can use "\t" just as you would use "\n" for new lines
- Remember: You can nest loops under loops (under loops, ...)
{% endspoiler %}

{% spoiler "Pseudo Solution" %}
- For character alignment you can use "\t" just as you would use "\n" for new lines
- Use a double for loop. Each counting to 10.
    - In the inner loop:
        - Multiply the numbers of both iterations.
        - Print the result and alignment character
    - In the outer loop:
        - Print a \n character

{% endspoiler %}





