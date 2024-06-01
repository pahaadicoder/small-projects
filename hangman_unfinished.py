HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

def hangman():
    word_list = ["banana", "apple", "pears", "jackfruit"]
    chosen_word = random.choice(word_list)
    guessed_letters = []
    attempts = 7

    while attempts > 0:
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("Current word: " + display_word)

        if display_word == chosen_word:
            print("Correct guess!")
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed this letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Right guess!")
        else:
            attempts -= 1
            print("Wrong guess. You lose a life.")
            if attempts < len(HANGMANPICS):
                print(HANGMANPICS[7 - attempts])

        if attempts == 0:
            print("GAME OVER! The word was:", chosen_word)
            break


hangman()
