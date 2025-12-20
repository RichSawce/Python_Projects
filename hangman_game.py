# store word as string
word = "doughnut"
# replace characters in word with "_"
codedWord = len(word) * "_"
# keep list of guessed letters
guessedLetters = []
# guesses left

print("Welcome to Hangman")
while True:
 print("Word: " + codedWord + "\nMisses: " + str(guessedLetters))
 letter = input("Guess a letter ")
# rebuild the "Word:_a___" display each turn by looping through the secret word
 if letter not in word:
    guessedLetters += [letter]
 if letter in word:
    codedWord = codedWord.replace("_", letter)
   

# Track wrong guesses by checking if guess not in secret_word

# end the game when too many wrong guesses or the word is completed.
