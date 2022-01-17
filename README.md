# Wordle Bot

Two different Selenium Python bots that solve Wordle Challenges.

The first bot plays a lot like a human. It starts with the word "adieu", and
from there it makes logical conclusions that help it find the answer, with it picking
the most frequently used word that matches all the known constraints. From my tests,
it has found the answer usually around 95% of the time.

The second bot takes a more strategic approach. It will always insert the words "first,"
"music," "black," and "phone." Then it will use all the information that those words give it to
find the answer (also from the word frequencies list). I've found that this bot is usually more 
accurate than the first bot, but it will always take at least 5 tries to get the answer, whereas 
the first bot can sometimes find the answer in 3 or 4 tries.

# Alternative Solvers

If you use any of these, make sure to drag them into the main directory.

Manual Solver:
I used this a lot for testing the logic before I actually implemented Selenium.
This can be a useful tool for testing the best strategies.

Auto Solver:
This just gets the answer automatically by finding it in the source code.
It's not very fun, but at least you will never lose :)

#

Credits to this website for the word frequency data: https://www.kaggle.com/rtatman/english-word-frequency
