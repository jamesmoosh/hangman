## hangman game
## 10/10/16 -jrkg

import random

dictionaryfile = open(dictionary.txt, r)
dictionary = []
## reject words <3, >8 letters long
for line in dictionaryfile:
    if len(line) > 5 and len(line) < 10:
        dictionary.append(line[:-2])
dict_length = len(dictionary)
dictionaryfiles.close()

## input random word from dictionary

def get_new_word(dict_length):
    line_number = random.randint(1,dict_length -1)
    word_to_guess = dictionary[line_number]
    return word_to_guess
     

working_word = str("_" * len(word_to_guess))
print("Word to guess is" working_word)
guesslist = []
correct_guesses = []
wrong_guesses = []
game_end = False

hangman_image = [
'''
  
      
      
    
     
        
       
========='''
,'''
  
       |
       |
       |
       |
       | 
       |
========='''
,'''
  ________
       |
       |
       |
       |
       | 
       |
========='''
,'''
  ________
   |   |
       |
       |
       |
       | 
       |
========='''
,'''
  ________
   |   |
   O   |
       |
       |
       | 
       |
========='''
,'''
  ________
   |   |
   O   |
   |   |
       |
       | 
       |
========='''
,'''
  ________
   |   |
   O   |
  /|   |
       |
       | 
       |
========='''
,'''
  ________
   |   |
   O   |
  /|\  |
       |
       | 
       |
========='''
,'''
  ________
   |   |
   O   |
  /|\  |
   /   |
       | 
       |
========='''
,'''
  ________
   |   |
   O   |
  /|\  |
   /\  |
       | 
       |
=========''']
hangman = hangman_image[0]
    
## check guess is a letter, and hasn't already been guessed. add to list of guesses
def get_guess(guesslist)
    while True:
        guess = str(input("Enter a letter to guess. "))
        guess = guess.lower
        if len(guess) != 1:
            print("Please enter a single letter")
        elif guess in guesslist:
            print("You've already guessed ", guess, ". Please choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return guess

## ask for guess
## check if guess is in word
## if yes, then new working word is  _ _ _ x _ replacing instances of letter. if word is complete then win
## if no add line to hangman. if hangman finished then lose
while True:
    if working_word != word_to_guess:
        print(hangman)
        print("The word you are guessing is ", working_word)
        print("You have already guessed these letters: ", guesslist)
        guess = get_guess(guesslist)
        guesslist.append(guess)
        if guess in word_to_guess:
            correct_guesses.append(guess)
            for i in range(len(word_to_guess)):
                if word_to_guess[i] in correct_guesses:
                    working_word = working_word[:i] + word_to_guess[i] + working_word[i+1:]
            print("Correct!)
        else:
            print("Sorry, that's wrong")
            wrong_guesses.append(guess)
            hangman = hangman_image[len(wrong_guesses)]
            if len(wrong_guesses) == 10:
                  print(hangman)
                  print("You have lost! The word was ", word_to_guess)
                  game_end = True
    else:
        print("Congratulations! You won!)
        game_end = True
    if game_end = True:
        again = input("Play again, Y/N?")
        if again.lower == "y":
            word_to_guess = get_new_word(dict_length)
            working_word = str("_" * len(word_to_guess))
            print("Word to guess is" working_word)
            guesslist = []
            correct_guesses = []
            wrong_guesses = []
            game_end = False
        else:
            break
