---
files: [isgif.c]
window: [terminal]
---
# Gif Checker
Write a program that checks if a file is (likely) a GIF (GIF 89a to be specific).
Note that the first six characters of a GIF 89a file are the characters:

```
G, I, F, 8, 9, a.
```
Usage: ./isgif filepath

Prints:
* If file is gif: "File is a gif"
* Otherwise: "File is not a gif"
