## hangman game
## 10/10/16 -jrkg

import random

dictionaryfile = open(dictionary.txt, r)
dict_length = sum(1 for line in dictionaryfile)
line_number = random.randint(1,dict_length)
dictionary = dictionaryfile.readlines()
dictionaryfiles.close()

## input random word from dictionary

def newword(line_number):
    word_to_guess = dictionary[line_number - 1]
    return word_to_guess[:-2]

word_to_guess = newword(line_number)

## reject words <3, >8 letters long

while len(word_to_guess)< 3 or len(word_to_guess) > 8:
    line_number = random.randint(1,dict_length)
    word_to_guess = newword(line_number)

## print _ _ _ (length of word)

working_word = str("_ " * len(word_to_guess))
print("Word to guess is" working_word)
guesslist = []

## ask for guess
while working_word == word_to_guess is False:
    guess = str(input("Enter a letter to guess. "))

## check guess is a letter, and hasn't already been guessed. add to list of guesses
    while True:
        if len(guess) == 1 is False:
            print("Please enter a single letter")
            guess = str(input("Enter a letter to guess. "))
    for letter in guesslist:
        if letter == guess:
            print("You've already guessed ", guess)
            guess = str(input("Enter a letter to guess. "))
    
    guesslist.append(guess)

## check if guess is in word

for letter in word_to_guess:
    if letter == guess:
        

## if yes, then new working word is  _ _ _ x _ replacing instances of letter. if word is complete then win

## if no add line to hangman. if hangman finished then lose

## print hangman

## print list of guesses

## print working word

## ask for guess
