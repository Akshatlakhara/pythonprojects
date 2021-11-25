# hangman game
import random


def hangman():
    word = random.choice(["wonderwoman", "blackwidow",
                         "agentcarter", "hulk", "spiderman", "batman", "thor"])
    validletter = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""
    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You win!!")
            break
        print(" guess the word:", main)
        guess = input()

        if guess in validletter:
            guessmade = guessmade + guess
        else:
            print("enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
            print("you have {} turns left".format(turns))
        if turns == 0:
            break


name = input("enter your name")
print("welcome ", name)

print("try to guess the name in less then 10 turns")
hangman()
print()
