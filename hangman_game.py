import sys
import random

# store word as string
list = ["doughnut", "python", "hangman", "challenge", "programming", "developer", "function", "variable"]
word = random.choice(list)
# replace characters in word with "_"
codedWord = len(word) * "_"
# keep list of guessed letters
guessedLetters = []
# guesses left
maxGuesses = 6
print("Welcome to Hangman")
while True:
 print("Word: " + codedWord + "\nMisses: " + str(guessedLetters) + "\nGuesses left: " + str(maxGuesses))
 letter = input("Guess a letter ").lower()
# validate input to ensure only one letter is entered at a time
 if len(letter) > 1 or not letter.isalpha():
      print("Enter one letter at a time")
   
# Track wrong guesses by checking if guess not in secret_word
 elif letter in guessedLetters:
       print("You already guessed that letter, try again.")
  
 elif letter not in word:
        guessedLetters += [letter]
        maxGuesses -= 1
    
# end the game when too many wrong guesses or the word is completed.
 if maxGuesses == 0:
      print("You lose! The word was " + word)
      sys.exit()
# rebuild the "Word:_a___" display each turn by looping through the secret word
 if letter in word:
      for i in range(len(word)):
         if word[i] == letter:
            codedWord = codedWord[:i] + letter + codedWord[i+1:]
            if "_" not in codedWord:
               print("You Win!" + "\nYou correctly guessed the word: " + word)
               sys.exit()

