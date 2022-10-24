# Name: Issa Mohamed
# Date: 10/15/2021
# Class: CS 111
# Prof: Aaron Bauer

import random

# a list of text-based pictures to illustrate the number of remaining guesses
hangman_pics = ["""
       
       
       
       
       
       
         """, """
       
       
       
       
       
       
=========""", """
       
       
       
      |
      |
      |
=========""", """
      +
      |
      |
      |
      |
      |
=========""", """
   ---+
      |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""]

TOTAL_GUESSES = 10  # constant for the total number of guesses the player gets


# a function to get the next letter from the user
# repeatedly prompts the user until valid input is entered
# requires that the input be a single letter, and not be a previously guessed letter
# the parameter guessed is a list of previously guessed letters
# returns the user's next guess
def get_guess(guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        # keep asking until we get a letter that hasn't been guessed
        if ((guess in guessed) or ( guess.isalpha() == False) or (len(guess) > 1)): 
            if (guess in guessed):
                msg = "You've already guessed that letter. "
                print(msg)
            elif (guess.isalpha() == False):
                msg = "That's not a letter. "
                print(msg)
            elif (len(guess) > 1):
                msg = "That is more than one letter. "
                print(msg)
        else:
            return guess


# a function to play a game of hangman
def play():
    # make a random choice from a file with one word per line
    word_file = open("wordlist.txt")
    word = random.choice(word_file.readlines())
    word = word.rstrip()
    word_file.close()

    current = [] # list of the user's current progress
    for c in word: # starts with no letters guessed, so a blank ("_") for each letter
        current.append("_")
    guessed = [] # list of previously guessed letters

    guesses = TOTAL_GUESSES # current number of guesses

    # while the user hasn't guessed the word and has guesses remaining
    while (("".join(current) != word) and (guesses > 0)):
        # display the current status of the game
        print("--------------------------------------------------")
        print(guesses, "guesses left")
        print(hangman_pics[TOTAL_GUESSES - guesses])
        print(" ".join(current))
        print("Letters you've already guessed:", " ".join(sorted(guessed)))
        print()

        # get the user's next guess, passing in the list of already guessed letters
        guess = get_guess(guessed)
        guessed.append(guess)

        if guess in word: # correct guess
            # replace the corresponding blanks in current with the guessed letter
            for i in range(len(word)):
                if guess == word[i]: # this location matches the guessed letter
                    current[i] = guess
        else: # incorrect guess
            guesses = guesses - 1

    # we've left the while loop, so the game is over
    # check whether the user won or lost
    if "".join(current) == word:
        print(" ".join(current))
        print("You win!")
    else:
        print("You lose. The word was", word)
        print(hangman_pics[-1])


play()