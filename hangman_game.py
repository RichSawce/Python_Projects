# store word as string
word = "doughnut"

# replace characters in word with "_"
codedWord = len(word) * "_"
# keep list of guessed letters
guessedLetters = []
# guesses left
maxGuesses = 6
print("Welcome to Hangman")
while True:
 print("Word: " + codedWord + "\nMisses: " + str(guessedLetters) + "\nGuesses left: " + str(maxGuesses))
 letter = input("Guess a letter ")
# Track wrong guesses by checking if guess not in secret_word
 if letter not in word:
    guessedLetters += [letter]
    maxGuesses -= 1
# end the game when too many wrong guesses or the word is completed.
    if maxGuesses == 0:
      print("You lose! The word was " + word)
      exit()
# rebuild the "Word:_a___" display each turn by looping through the secret word
 if letter in word:
      for i in range(len(word)):
         if word[i] == letter:
            codedWord = codedWord[:i] + letter + codedWord[i+1:]
