# HANGMAN GAME

import random

def hangman():
    
    words = ["python", "hangman", "coding", "developer", "algorithm", "function"]
    word_to_guess = random.choice(words)  
    guessed_word = ["_"] * len(word_to_guess)  
    guessed_letters = set()  
    max_attempts = 5
    attempts = 0  

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You have", max_attempts, "incorrect guesses allowed.")
    print("Word:", " ".join(guessed_word))

    while attempts < max_attempts and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good job! That letter is in the word.")
            
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Oops! That letter is not in the word.")
            attempts += 1
            print(f"Incorrect guesses left: {max_attempts - attempts}")

        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word:", word_to_guess)
    else:
        print("Game over! The word was:", word_to_guess)

hangman()

