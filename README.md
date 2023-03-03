# jklm-bot
💻 Simple jklm.fun bot which finds correct word from a list.


## What is jklm?
jklm.fun is a site where you have to guess English words
that contain the given syllable. I made a script that fetches a syllable by copying it
from the page and searching for words corresponding to it in wordlist.txt, which contains
approx. 60,000 English words.


## Installing dependencies
```
pip install keyboard
pip install pynput
```


## Usage
The script currently works with F2, F4, F8, F9 and F10 keys. Cursor must be
on the jklm.fun site ON **TOP OF THE SYLLABLE** on and the screen resolution must not be too small or the page zoomed.
The script retrieves the byte and writes it automatically at a speed suitable for the function.

Note that I have made this script for myself so that it works for my personal needs. That is the reason why usage is so messed up and complicated.


## Functions
The script has five different functions.
     - Realistic speed with errors [F2]
     - Realistic speed without errors [F4]
     - Faster than realistic speed without error [F8]
     - Very fast speed without errors [F9]
     - Realistic speed with longest word [F10]
