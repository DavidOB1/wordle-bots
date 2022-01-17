# Wordle Bot

A Selenium Python bot that solves the game Wordle.
It completes the game about 95% of the time, but it does occasioanlly fail.
It first uses the given text file, which has words sorted by their usage.
It sorts through the file, and then throughout the game it makes logical deductions
from the info given by the guesses to guess the next word, which it gets by picking the
first word from the new filtered list.
I start each round with the word "adieu" since it gives a lot of info on which vowels are
used, although you can really start with any word you'd like.

# Manual Solver

If you try to use this, make sure wordle-words.txt is in the same directory as the file.
I used this a lot for testing the logic before I actually implemented selenium.
This can be a useful tool for testing the best strategies.

# Auto Solver

This just gets the answer automatically by finding it in the source code.
It's not very fun, but at least you will never lose :)

Note: wordle-words.txt does not contain exclusively words for wordle, it has 1/3 of a million words
sorted by their frequencies. This can be useful for other projects.
Credits to this website for that data: https://www.kaggle.com/rtatman/english-word-frequency
