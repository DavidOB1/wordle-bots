import random


with open("wordle-words.txt") as f:
  wDict = f.read().splitlines() 

wDict = [word.split(",")[0] for word in wDict]
wDict = [word for word in wDict if len(word) == 5]


print("Manual Wordle Solver")
print("--------------------")
print("Your first input should be \"adieu\".")
print("If the letter is gray, prefix it with /")
print("Example: /a\n")
print("If the letter is yellow, prefix it with ?")
print("Example: ?d\n")
print("If the letter is green, prefix it with !")
print("Example: !e\n")
print("If you solved it, type /done")
print("Okay, after you enter the first word, fill out the following:\n")


def getLetters():
    x1 = input("First letter: ")
    if x1 == "/done":
        print("Nice!")
        quit()
    x2 = input("Second letter: ")
    x3 = input("Third letter: ")
    x4 = input("Fourth letter: ")
    x5 = input("Fifth letter: ")
    return [x1, x2, x3, x4, x5]


possible_words = wDict
def_has_this = []
for q in range(5):
    letters = getLetters()
    for i in range(5):
        letter = letters[i]
        bool1 = (letter[0] == "?") or (letter[0] == "!")
        bool2 = bool1 and (not letter in def_has_this)
        if bool2:
            def_has_this.append(letter[1].lower())
    for i in range(5):
        letter = letters[i]
        if letter[0] == "?":
            possible_words = [x for x in possible_words if letter[1].lower() in x]
            possible_words = [x for x in possible_words if x[i] != letter[1].lower()]
        elif letter[0] == "!":
            possible_words = [x for x in possible_words if letter[1].lower() == x[i]]
        elif letter[0] == "/":
            if letter[1] in def_has_this:
                possible_words = [x for x in possible_words if x.count(letter[1].lower()) == 1]
                possible_words = [x for x in possible_words if x[i] != letter[1].lower()]
            else:
                possible_words = [x for x in possible_words if not letter[1].lower() in x]
    try_word = possible_words[0]
    print("Okay, try this word: " + try_word)


if input("Were you able to get it? ").lower() == "yes":
    print("Nice!")
else:
    print("Darn.")

